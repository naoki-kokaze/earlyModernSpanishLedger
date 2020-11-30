# 近世スペイン複式簿記史料マークアップのためのガイドライン（暫定版）| Tentative Guideline for Mark-up of Early Modern Spanish Double-Bookkeeping Ledger
Last updated on 30th November 2020

### 小風尚樹（千葉大学）・伏見岳志（慶応義塾大学）・中村雄祐（東京大学）
### Naoki Kokaze (Chiba University), Takeshi Fushimi (Keio University), and Yusuke Nakamura (The University of Tokyo)


このページでは、近世スペインの元帳史料を分析するためのソースコードやマークアップファイルを公開しており、学会（人文科学とコンピュータシンポジウム 「じんもんこん2020」）の発表資料の補足情報として閲覧・活用可能にすることを目的としています。

This repository contains a set of programming codes and mark-up files for analysing an early modern Spanish ledger. A purpose for publishing this repository is to make them available as the appendix for the conference paper of Jinmoncom 2020.
***

このページで閲覧できる情報は、史料の撮影画像以外は、クリエイティブ・コモンズ・ライセンスBY4.0にて提供します。関心ある方からのご意見・コメントをいただければ幸いです。

You can make use of this material, other than the source images, under the license of CC BY 4.0 
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="クリエイティブ・コモンズ・ライセンス" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>, and I would be happy to have some feedback from those who are interested in using them.

## 発表概要 | Abstract of the Presentation
本発表では，近年国際的に議論が進んでいる会計史料のマークアップ手法DEPCHAを参照しながら，16世紀北スペインの元帳史料を構造化した．具体的な成果として，(1) 元帳における借方と貸方の取引収支が釣り合っていることを表現する必要性からDEPCHAの現行モデルの限界を指摘したこと，(2) 当該史料における人物名や勘定関連の用語法・情報の空間的配置・記述の信頼性を考察したこと，(3) そしてマークアップのガイドラインを公開したことが挙げられる．今後の課題は，本研究の成果やマークアップのガイドラインを国際的に議論する材料として改善することである．

We are developing a guideline for the markup of early modern Spanish historical accounts using DEPCHA, an extended TEI schema specialized in historical account books proposed by Georg Vogeler. In this presentation, we report the results of our markup of a ledger prepared by Salamanca family in 16th-century Spain on the dates of transaction, spellings of personal names and account categories, and point out several constraints of the current DEPCHA scheme. The first version of our guideline is available on GitHub.


## マークアップファイル | Markup File

<a href="markup_guideline/markup_guideline_publish.md">16世紀北スペイン、サラマンカ商会元帳のマークアップ例</a>

<a href="markup_guideline/markup_guideline_publish.md">Markup Example of the Ledger of the <i>Compañia de los Salamanca</i> in Northern Spain in the 16th Century</a>


## 分析結果 | Results of Analysis

### 1. 人名表記のゆれと略記 | Variations on the Names of People mentioned in the Ledger

表記のゆれへの対応は一般にテキストのマークアップの重要項目であるが，信用が重視される会計簿においては，名称，特に人名表記の安定性は極めて重要である．元帳で言及された45人を分析したところ，表記のゆれ幅は，個人の同定が困難になるほどではなかった．16世紀において人名などの綴りにはゆれが見られる．正書法が確立していない時代のため，ゆれがあることは当然である．さらに，当時の文書では，さまざまな単語が略記される傾向があった．たとえば，下記の表ではSalamancaがsaと略記されるケースがある．

この統一表記を付与する作業は，別の分析の可能性を拓く．すなわち，どのような人物の場合にゆれが大きくなるか，である．表では，ゆれが大きいのは最初の3名である．このうちMiguel de Salamancaはサラマンカ商会の成員である．また，残り2名（Alonso de BeguillasとPedro de Caballos）については，取引内容の検討から，サラマンカ商会の業務である羊毛の買い付けや運搬を担う人物であり，いわば関係者だと判断される．したがって，商会の関係者のほうがゆれが大きいという推測が成り立つ．

|統一表記|表記のバリエーション|
|---|---|
|Miguel de Salamanca|migl de sa; miguel de sa; miguel de sa; miguel de salamanca; migel de sa|
|Alonso de Beguillas|Alonso de beguillas; ao de beguillas; ao de beguillas; ao de beguillas; ao de beguillas|
|Pedro de Caballos|po de cauallos; po de cauallos; cauallos; cauallos|
|Pedro López|po Lopez; le; les|
|Joan de Ezcaray|Jhoan Dezcaray; le|
|Francisco y Andrés Hernández|franco y andres hrres; franco y andres Hrres|
|Marcos de Hernández|marcos hernandez; marcos hernandez|
|Andrés Martín|andres martin; andres martin|
|García de Salamanca|garcia De Salamanca|
|Benito Hernández|Benito hernandez|
|Gregorio López de Lozoya|go lopez de Lozoya|
|Bartolomé Belázquez|bartolome belazquez|
|Joan de Herrera|Joan de herrera|
|Antonio Cerezo|antonio cerezo|
|Antonio Martín|anton martin|
|Joan Herreros y Alonso Pérez|Jno hrres y as perez|
|Alonso Martín de Arriva|alo min de arriua|
|Fruto López y María López su madre|frutos Lopez y mari Lopez su madre|
|Antonio Pedro Corral|antonio po corral|
|Martín de Sancho|min de sancho|
|Joan Gamo y Pedro Braojos|Jno gamo y po braojos|
|Joan del Pozo|Joan del pozo|
|Andrés Sainz de Villorojo|andres Sainz de Villorejo|
|Joan Sainz|Joan Sainz|
|Martín de Carnezia|min de carnezia|
|Joan de Ezcaray de Lozoya|Joan dezcaray de Lozoya|
|Joan Martín de Lozoya|Jhoan min de Lozoya|
|Joan Hernández|Joan hernandez|
|Francisco Martín de Luzía|franco min de luzia|
|Joan Pérez de Pradano|Joan perez de pradano|
|Joan González|Joan gonzalez|
|Frutos Calvo|frutos caluo|
|Antonio González Guillen|anton ges guillen|
|Joan Sánchez de Peña|Joan Sanchez de pena|
|Gregorio de Santa María|Gregorio de santa maria|
|Pero Blazquez|pero blazquez|
|el Comendador y fráiles|comendador y freires|
|Antonio de la Mata y compañía|anton de la mata e conpa|
|Antonio y Pedro Corral|Antonio y po corral|
|Miguel y Joan Sánchez|migel y Joan sanchez|
|Lucas López de Penilla|lucas lopez de penilla|
|Pasqual Sánchez|pasqual sanchez|
|Joan y Pedro Hernández|Jhoan y po hrres|
|Joan de Pero Sainz|Joan de pero sainz|
|Joan Sainz el viejo|Joan Sainz el biejo

### 2. 「勘定科目」の語彙の出現パターン | Occurrence Patters of 'Accounting' Vocabularies

DEPCHAで定義されている@ana属性値bk:accountを使って，当時の勘定に関する語彙（厳密には現代の会計概念における勘定科目とは一致しないが，以下では便宜的に「勘定科目」と呼ぶ）を抽出した結果を下記の表に示す．帳簿を仔細に検討すると，それぞれの表現が用いられる頻度の差は，それぞれの表現がデータセット内のどの位置で用いられるかによって説明できることが明らかになった．

各セットのなかに複数の取引が含まれる場合，1件目の取引では借方記入 (deue) や貸方記入 (A de auer) といった会計用語が用いられる．しかし，2件目の取引以降は，支払った (pago) ，渡した (dio) といった一般的な表現が用いられる．ここから，2件目以降の表現は，1件目の会計用語と同じ意味で用いられていると判断される．したがって，一般的な表現のあいまいさは，そのセットの1件目の取引を参照することによって解消される．

|仕訳番号|借方欄の「勘定科目」|貸方欄の「勘定科目」|
|---|---|---|
|1|deue|A de auer|
|1|dio|dio|
|1|dio|dio|
|1|dio|dio|
|1|dio|dio|
|1||dio|
|1||dio|
|1||dio|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||pago|
|1||dio|
|1||dio|
|2|deue|A de auer|
|2|dio||
|3|deuen|An de auer|
|3||dio|
|4|deuen|An de auer|
|4|dio||
|5|deuen|An de auer|
|5|dio||

### 3. 取引収支の分析 | Analysis on the Balance of Payment
本研究では元帳の仕訳における借方と貸方の取引収支が釣り合っているかどうかを確認できるように，取引金額のローマ数字をアラビア数字に変換した値をデータとして保持していた．このデータをもとに，元帳の35ページにおける取引収支を検算した結果の一部を下記の表に示す．

検算結果は，帳簿に記載された収支の額と合致していた．このことは，この帳簿においては，金額やその合計額の算出が正確におこなわれており，商会の人間が正確性を重視したことを示唆している．

|debit side||||||credit side||||||
|---|---|---|---|---|---|---|---|---|---|---|---|
|entry No.|text|status|amount|sum|check BP|entry No.|text|status|amount|sum|check BP|
|entry.1|+Alonso de beguillas deue En pro de Henero 170 U que so^ Por el rrsto de/otra su quenta del libro viejo de los negos De rroan de compa que son por 5 U rres que le dio migl de sa para Lleuar a la sierra de Pedraza como pez en el dho libro a fo l_320|deue|170000|||entry.1|+ A de auer En pro de Heno 37 U 500 que son por tantos dio de contado a frutos Lopez y mari Lopez su madre l_20|A de auer|37500|||
|entry.1|+ en este dia 170 U que son por 5 U rres que por cedula de garcia De Salamanca le dio Gregorio de santa maria pez l_29|dio|170000|||entry.1|+ en este dia 74 U 800 que dio de qo a antonio cerezo l_34|dio|74800|||
|entry.1|+ en este dia 170 U que son por 5 U rres los 4 U que sobro de po Lopez canuio por ca de miguel de sa e los 1 U rres que le dio el dho miguel para lleuar a la dha sierra como pez l_17|dio|170000|||entry.1|+ en este dia 71 U 400 que dio a go lopez de Lozoya pze l_34|dio|71400|||
|entry.1|+ en este dia 646 U que son por 19 U rreales que le dio el dho miguel de sa la segunda bez que fue a la dha sierra l_27|dio|646000|||entry.1|+ en este dia 17 U 408 que dio a Joan de pero sainz pze l_34|dio|17408|||
|entry.1|+ en este dia 102 U que son por 3 U rreales que les dio el dho miguel de salamanca la tercera bez q boluio a dha sa l_27|dio|102000|||entry.1|+ en este dia 4 U 488 que dio a lucas lopez de penilla l_34|dio|4488|||
|entry.1|||1258000|1258000|TRUE|entry.1|+ en este dia 1 U 700 que dio a Joan dezcaray de Lozoya l_35|dio|1700|||
|||||||entry.1|+ en este dia 105 U 400 que dio a franco y andres hrres l_35|dio|105400|||
|||||||entry.1|+ en este dia 115 U 600 que dio a Joan hernandez l_35|dio|115600|||
|||||||entry.1|+ en este dia 17 U que pago a antonio po corral pze l_35|pago|17000|||
|||||||entry.1|+ en este dia 10 U 200 que pago a bartolome belazquez pze l_36|pago|10200|||
|||||||entry.1|+ en este dia 10 U 200 que pago a andres martin pze l_36|pago|10200|||
|||||||entry.1|+ en este dia 2 U 040 que pago a min de carnezia l_36|pago|2040|||
|||||||entry.1|+ en este dia 8 U 500 que pago a Jno hrres y as perez pze l_36|pago|8500|||
|||||||entry.1|+ en este dia 10 U 200 que pago a Joan del pozo pze l_37|pago|10200|||
|||||||entry.1|+ en este dia 5 U 100 que pago a Jhoan min de Lozoya l_37|pago|5100|||
|||||||entry.1|+ en este dia 408 que pago a Benito hernandez pze l_37|pago|408|||
|||||||entry.1|+ en este dia 81 U que pago a pasqual sanchez pze l_37|pago|81000|||
|||||||entry.1|+ en este dia 22 U 100 que pago a po min de sancho po l_38|pago|22100|||
|||||||entry.1|+ en este dia 34 U que pago a marcos hernandez l_38|pago|34000|||
|||||||entry.1|+ en este dia 7 U que pago a andres Sainz de Villorejo l_38|pago|7000|||
|||||||entry.1|// // //||636044|636044|TRUE|
|||||||entry.1|+ en este dia 1 U 734 que pago a Joan Sainz el biejo l_38|pago|1734|||
|||||||entry.1|+ en este dia 2 U 992 que pago a Jno gamo y po braojos l_39|pago|2992|||
|||||||entry.1|+ en este dia 12 U 920 que pago a anton martin pze l_39|pago|12920|||
|||||||entry.1|+ en este dia 12 U 170 que pago a Joan Sainz scriuano l_39|pago|12170|||
|||||||entry.1|+ en este dia 45 U que pago a migel y Joan sanchez l_39|pago|45000|||
|||||||entry.1|+ en este dia 40 U que pago a andres martin paze l_40|pago|40000|||
|||||||entry.1|+ en este dia 23 U 800 que pago a Joan perez de pradano l_40|pago|23800|||
|||||||entry.1|+ en este dia 17 U que pago a Joan Sanchez de pena l_40|pago|17000|||
|||||||entry.1|+ en este dia 6 U 800 que pago a frutos caluo pze l_40|pago|6800|||
|||||||entry.1|+ en este dia 119 U que pago a anton ges guillen paze l_41|pago|119000|||
|||||||entry.1|+ en este dia 34 U que pago a A franco min de luzia l_41|pago|34000|||
|||||||entry.1|+ en este dia 20 U 400 que pago a Joan gonzalez paze l_41|pago|20400|||
|||||||entry.1|+ en este dia 54 U 400 que pago a pero blazquez paze l_41|pago|54400|||
|||||||entry.1|+ en este dia 10 U 200 que pago a alo min de arriua l_42|pago|10200|||
|||||||entry.1|+ en este dia 85 U que pago a marcos hernandez paze l_42|pago|85000|||
|||||||entry.1|+ en este dia 10 U 200 que pago a anton de la mata e conpa l_42|pago|10200|||
|||||||entry.1|+ en este dia 10 U 200 que pago a Joan de herrera paze l_42|pago|10200|||
|||||||entry.1|+ en este dia 68 U que pago al comendador y freires l_43|pago|68000|||
|||||||entry.1|+ en este dia 22 U 199 que dio por qa aber echo de costas en la dha sierra en la conpra de la lana como paze l_44|dio|22199|||
|||||||entry.1|+ en este dia 25 U 941 q^ dio de qo a migel de sa pa fin de su qa l_27|dio|25941|||
|||||||entry.1|||1258000|1258000|TRUE|
|entry.2|+ Jhoan Dezcaray vzo de lozoya deue En pro de Heno 1 U 700 que le dio ao de beguillas para señal y pte de pago de 50 lanas q^ le compro a 68 cada lana a pagar el rrsto al rreciuo l_22|deue|1700|||entry.2|+ A de auer En 9 de junio 3 U 400 que son por 50 las q^ Dio este rreciuo a 68 lana q es lo dicho pez l_33|A de auer|3400|3400|TRUE|
|entry.2|+ en 9 de junio 1700 q^ le dio po de cauallos pa fin desta qa l_31|dio|1700|||||||||
|entry.2|||3400|3400|TRUE|||||||
|entry.3|+ franco y andres Hrres Vzos de braojos deuen En pro de Heno 105 U 400 que le dio ao de beguillas para señal y parte de Pago de 1 U 500 lanas que le conpro las 1 U 400 estreme Nas a 83 y 100 lanas churras a 73 rrsto sobre saca l_22|deuen|105400|105400|TRUE|entry.3|+ An de auer En 9 de junio 100 U 386 que son por 1 U 118 les estremenas a 83 que son 92 U 794 y 104 lanas churras a 73 que son 7 U 592 que dio este rreciuo que es lo dho l_33|An de auer|100386|||
|||||||entry.3|+ en 8 de nouie 5 U 014 que dio de contado a po de cauallos|dio|5014|||
|||||||entry.3|||105400|105400|TRUE|
|entry.4|+ Jhoan y po hrres Vzos de braojos deuen en pro de heno 115 U 600 que les dio ao de beguillas pa señal y pre de pago de 2 U 200 ls que les conpro las 1 U dellas 50 mas a mos de las caidas el ano pasdo y 1 U 100 de ogano a 80 mrs cada lana mos 500 mrs En todo a pagar el rresto sobresaca como pez l_22|deuen|115600|||entry.4|+ An de auer En 9 de junio 172 U 140 que son por 2 U 158 lanas q^ dieron este rreciuo a 80 mrs cada lana con 500 mrs que se le rrebaten es lo dicho como paresce l_33|An de auer|172140|172140|TRUE|
|entry.4|+ en 9 de junio 56 U 540 q^ le dio cauallos pa fin desta qa l_31|dio|56540|||||||||
|entry.4|||172140|172140|TRUE|||||||
|entry.5|+ Antonio y po corral vzso de braojos deuen En pro de Heno 17 U q les dio ao de beguillas pa senal y pte de pago de 400 las De los conpro a 78 1/2 la lana a pagar el rrsto sobre saca l_22|deuen|17000|||entry.5|+ An de auer En 9 de junio 31 U 714 que son por 404 lanas q dieron este rreciuo a 78 1/2 cada lana que es lo dho l_33|An de auer|31714|31714|TRUE|
|entry.5|+ en 9 de junio 14 U 714 que le dio cauallos pa fin desta qa l_31|dio|14714|||||||||
|entry.5|||31714|31714|TRUE|||||||

