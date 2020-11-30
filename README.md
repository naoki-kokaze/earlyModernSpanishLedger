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

1. 人名表記のゆれと略記 | Variations on the Names of People mentioned in the Ledger

表記のゆれへの対応は一般にテキストのマークアップの重要項目であるが，信用が重視される会計簿においては，名称，特に人名表記の安定性は極めて重要である．元帳で言及された45人を分析したところ，表記のゆれ幅は，個人の同定が困難になるほどではなかった．

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

2. 「勘定科目」の語彙の出現パターン | Occurrence Patters of 'Accounting' Vocabularies

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


