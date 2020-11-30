import bs4, re

f_input = open("burgos_ledger.xml", "rb")
soup = bs4.BeautifulSoup(f_input, 'xml')
f_input.close()

# まずは日付の分布を分析する
def date_extract(soup):
    dates = soup.select('date[ana="bk:when"]')
    date_distribution_dict = {}
    for date in dates:
        date_greg = date["when"]
        if date_greg not in date_distribution_dict.keys():
            date_distribution_dict[date_greg] = 1
        else:
            date_distribution_dict[date_greg] += 1
    
    return date_distribution_dict


# 人物の出現状況の一覧作成
def listup_persons(soup):
    persons = soup.select('person')
    name_dict = {}
    spaces = re.compile(r'\s{2,}')
    for person in persons:
        name_list = []
        name_ref = f'#{person["xml:id"]}'
        name_references = soup.body.select(f'persName[ref="{name_ref}"]')
        for ref in name_references:
            name_list.append(re.sub(spaces, ' ', ref.text.strip()))
        name_dict[person.text.strip()] = name_list

    return name_dict


# bk:statusの語彙一覧を取得する
def listup_vocab_status(soup):
    statuses = soup.select('span[ana="bk:status"]')
    result = {}
    for status in statuses:
        vocab = status.text
        if vocab not in result.keys():
            result[vocab] = 1
        else:
            result[vocab] += 1

    return result


# bk:statusの語を取得する関数
def extract_status(row):
    if row.select('span'):
        status = row.select_one('span').text
    else:
        status = ''
    return status


# 金額の収支を確認できる関数群を作る。済
def debit_credit_output(rows):
    # formatting関数の中の細かい処理。resultは文字列型
    result = ''
    spaces = re.compile(r'\s{2,}|\n')
    # 検算のための変数
    check_sum = 0

    for index, row in enumerate(rows):
        # 本文部分とentry ID、bk:statusの値を抽出する
        if row.select_one('cell[ana="desc"]'):
            desc = row.select_one('cell[ana="desc"]').text.strip()
            desc = desc.replace("+", "'+")
            desc = re.sub(spaces, ' ', desc)
        else:
            desc = ''
        n = row.parent.parent.parent['n']
        status = extract_status(row)
        result += f'entry.{n}\t{desc}\t{status}\t'

        if row.select_one('cell[ana="amount"]'):
            amount = row.select_one('cell[ana="amount"]')
            result += amount.measure["quantity"] + '\n'
            check_sum += int(amount.measure["quantity"])
        elif row.select_one('cell[ana="sum"]'):
            sum_element = row.select_one('cell[ana="sum"]')
            check_BP = check_sum == int(sum_element.measure["quantity"])
            result += str(check_sum) + '\t' + sum_element.measure["quantity"] + '\t' + str(check_BP) + '\n'
        elif row.select_one('cell[ana="amount sum"]'):
            sum_amount = row.select_one('cell[ana="amount sum"]')
            result += sum_amount.measure["quantity"] + '\t' + sum_amount.measure["quantity"] + '\n'
        print(f'{index}行はOK')

    return result
    

def formatting(entries, f_output):
    for entry in entries:
        debit = entry.select_one('div[ana="bk:debit"]')
        credit = entry.select_one('div[ana="bk:credit"]')
        d_rows = debit.select('row')
        c_rows = credit.select('row')
        
        d_result = debit_credit_output(d_rows)
        c_result = debit_credit_output(c_rows)

        f_output.write('debit side\ttext\tstatus\tamount\tsum\tcheck BP\n')
        f_output.write(d_result)
        f_output.write('credit side\ttext\tstatus\tamount\tsum\tcheck BP\n')
        f_output.write(c_result)

    f_output.close()
    return None


def check_debit_credit(soup, f_output):
    # entryごとにdivを分ける
    entries = soup.select('div[ana="entry"]')
    formatting(entries, f_output)
    return None
        
        
        	
