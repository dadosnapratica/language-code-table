# Language Codes Repository

## Purpose
This repository contains a table of language codes, including English names, native names, subtags, and URLs to country flags. The table aims to provide an easily accessible reference for language identification codes aligned with IETF standards.

## Table of Contents

- [Purpose](#purpose)  
- [Standards](#standards)  
- [Usage of Language Codes](#usage-of-language-codes)
- [Language Code Table](#language-code-table)
- [Direct Links to Data and Schema](#direct-links-to-data-and-schema)  
- [Examples of Language Code Usage in Programming](#examples-of-language-code-usage-in-programming)  
   - [HTML](#html)  
   - [JavaScript](#javascript)  
   - [Python](#python)  
   - [Java](#java)  
   - [.NET](#net)  
   - [Use in Google Speech API](#use-in-google-speech-api)  
- [Licensing](#licensing)  
- [Reporting Issues](#reporting-issues)  
- [Contributing](#contributing)  
- [How to Citation](#citation)  
- [Utilization of AI in This Project](#utilization-of-ai-in-this-project)  
- [References](#references)  
- [Final Notes](#final-notes)  
- [Author](#author)  
- [Contact](#contact)

## Standards
The language codes and tags conform to the Internet Engineering Task Force (IETF) standards, specifically those outlined in BCP 47 and RFC 4646.

## Usage of Language Codes
Language codes are used to identify the language of content in various applications across computing and internet communications, enhancing global interoperability.

## Language Code Table
|Language Country Name       |English Name       |Portuguese-BR Name |Native Name                  |Subtag|Country Flag URL                    |
|----------------------------|-------------------|-------------------|-----------------------------|------|------------------------------------|
|South Africa                |Afrikaans          |Africâner          |Afrikaans                    |af    |https://flagcdn.com/16x12/za.png    |
|Ethiopia                    |Amharic            |Amárico            |አማርኛ                         |am    |https://flagcdn.com/16x12/et.png    |
|Arab League                 |Arabic             |Árabe              |العربية                      |ar    |https://flagcdn.com/16x12/ae.png    |
|Chile                       |Mapudungun         |Mapudungun         |Mapudungun                   |arn   |https://flagcdn.com/16x12/cl.png    |
|Morocco                     |Moroccan Arabic    |Árabe Marroquino   |الدارجة المغربية             |ary   |https://flagcdn.com/16x12/ma.png    |
|India                       |Assamese           |Assamês            |অসমীয়া                      |as    |https://flagcdn.com/16x12/in.png    |
|Azerbaijan                  |Azerbaijani        |Azeri              |Azərbaycan                   |az    |https://flagcdn.com/16x12/az.png    |
|Russia                      |Bashkir            |Baxkir             |Башҡорт                      |ba    |https://flagcdn.com/16x12/ru.png    |
|Belarus                     |Belarusian         |Bielorrusso        |беларуская                   |be    |https://flagcdn.com/16x12/by.png    |
|Bulgaria                    |Bulgarian          |Búlgaro            |български                    |bg    |https://flagcdn.com/16x12/bg.png    |
|Bangladesh                  |Bengali            |Bengalês           |বাংলা                        |bn    |https://flagcdn.com/16x12/bd.png    |
|Tibet                       |Tibetan            |Tibetano           |བོད་ཡིག                      |bo    |https://flagcdn.com/16x12/cn.png    |
|France                      |Breton             |Bretão             |brezhoneg                    |br    |https://flagcdn.com/16x12/fr.png    |
|Bosnia and Herzegovina      |Bosnian            |Bósnio             |bosanski/босански            |bs    |https://flagcdn.com/16x12/ba.png    |
|Spain                       |Catalan            |Catalão            |català                       |ca    |https://flagcdn.com/16x12/es.png    |
|Iraq                        |Central Kurdish    |Curdo Central      |کوردیی ناوەندی               |ckb   |https://flagcdn.com/16x12/iq.png    |
|Italy                       |Corsican           |Córsico            |Corsu                        |co    |https://flagcdn.com/16x12/it.png    |
|Czech Republic              |Czech              |Tcheco             |čeština                      |cs    |https://flagcdn.com/16x12/cz.png    |
|Wales (UK)                  |Welsh              |Galês              |Cymraeg                      |cy    |https://flagcdn.com/16x12/gb-wls.png|
|Denmark                     |Danish             |Dinamarquês        |dansk                        |da    |https://flagcdn.com/16x12/dk.png    |
|Germany                     |German             |Alemão             |Deutsch                      |de    |https://flagcdn.com/16x12/de.png    |
|Sorbia (Germany)            |Lower Sorbian      |Baixo Sorábio      |dolnoserbšćina               |dsb   |https://flagcdn.com/16x12/de.png    |
|Maldives                    |Divehi             |Divehi             |ދިވެހިބަސް                   |dv    |https://flagcdn.com/16x12/mv.png    |
|Greece                      |Greek              |Grego              |Ελληνικά                     |el    |https://flagcdn.com/16x12/gr.png    |
|USA, UK, etc.               |English            |Inglês             |English                      |en    |https://flagcdn.com/16x12/us.png    |
|Spain                       |Spanish            |Espanhol           |español                      |es    |https://flagcdn.com/16x12/es.png    |
|Estonia                     |Estonian           |Estoniano          |eesti                        |et    |https://flagcdn.com/16x12/ee.png    |
|Basque Country              |Basque             |Basco              |euskara                      |eu    |https://flagcdn.com/16x12/es-pv.png |
|Iran                        |Persian            |Persa              |فارسى                        |fa    |https://flagcdn.com/16x12/ir.png    |
|Finland                     |Finnish            |Finlandês          |suomi                        |fi    |https://flagcdn.com/16x12/fi.png    |
|Philippines                 |Filipino           |Filipino           |Filipino                     |fil   |https://flagcdn.com/16x12/ph.png    |
|Faroe Islands               |Faroese            |Feroês             |føroyskt                     |fo    |https://flagcdn.com/16x12/fo.png    |
|France                      |French             |Francês            |français                     |fr    |https://flagcdn.com/16x12/fr.png    |
|Netherlands                 |Frisian            |Frísio             |Frysk                        |fy    |https://flagcdn.com/16x12/nl.png    |
|Ireland                     |Irish              |Irlandês           |Gaeilge                      |ga    |https://flagcdn.com/16x12/ie.png    |
|Scotland (UK)               |Scottish Gaelic    |Gaélico Escocês    |Gàidhlig                     |gd    |https://flagcdn.com/16x12/gb-sct.png|
|Kiribati                    |Gilbertese         |Gilbertês          |Taetae ni Kiribati           |gil   |https://flagcdn.com/16x12/ki.png    |
|Galicia (Spain)             |Galician           |Galego             |galego                       |gl    |https://flagcdn.com/16x12/es-ga.png |
|Switzerland                 |Swiss German       |Alemão Suíço       |Schweizerdeutsch             |gsw   |https://flagcdn.com/16x12/ch.png    |
|India                       |Gujarati           |Guzerate           |ગુજરાતી                      |gu    |https://flagcdn.com/16x12/in.png    |
|Nigeria                     |Hausa              |Haúça              |Hausa                        |ha    |https://flagcdn.com/16x12/ng.png    |
|Israel                      |Hebrew             |Hebraico           |עברית                        |he    |https://flagcdn.com/16x12/il.png    |
|India                       |Hindi              |Hindi              |हिंदी                        |hi    |https://flagcdn.com/16x12/in.png    |
|Croatia                     |Croatian           |Croata             |hrvatski                     |hr    |https://flagcdn.com/16x12/hr.png    |
|Yugoslavia (historical)     |Serbo-Croatian     |Sérvio-Croata      |srpskohrvatski/српскохрватски|hrv   |[Historical]                        |
|Sorbia (Germany)            |Upper Sorbian      |Alto Sorábio       |hornjoserbšćina              |hsb   |https://flagcdn.com/16x12/de.png    |
|Hungary                     |Hungarian          |Húngaro            |magyar                       |hu    |https://flagcdn.com/16x12/hu.png    |
|Armenia                     |Armenian           |Armênio            |Հայերեն                      |hy    |https://flagcdn.com/16x12/am.png    |
|Indonesia                   |Indonesian         |Indonésio          |Bahasa Indonesia             |id    |https://flagcdn.com/16x12/id.png    |
|Nigeria                     |Igbo               |Ibo                |Igbo                         |ig    |https://flagcdn.com/16x12/ng.png    |
|China                       |Yi                 |Yi                 |ꆈꌠꁱꂷ                         |ii    |https://flagcdn.com/16x12/cn.png    |
|Iceland                     |Icelandic          |Islandês           |íslenska                     |is    |https://flagcdn.com/16x12/is.png    |
|Italy                       |Italian            |Italiano           |italiano                     |it    |https://flagcdn.com/16x12/it.png    |
|Canada                      |Inuktitut          |Inuktitut          |Inuktitut/ᐃᓄᒃᑎᑐᑦ (ᑲᓇᑕ)       |iu    |https://flagcdn.com/16x12/ca.png    |
|Japan                       |Japanese           |Japonês            |日本語                          |ja    |https://flagcdn.com/16x12/jp.png    |
|Georgia                     |Georgian           |Georgiano          |ქართული                      |ka    |https://flagcdn.com/16x12/ge.png    |
|Kazakhstan                  |Kazakh             |Cazaque            |Қазақша                      |kk    |https://flagcdn.com/16x12/kz.png    |
|Greenland                   |Greenlandic        |Groenlandês        |kalaallisut                  |kl    |https://flagcdn.com/16x12/gl.png    |
|Cambodia                    |Khmer              |Khmer              |ខ្មែរ                        |km    |https://flagcdn.com/16x12/kh.png    |
|India                       |Kannada            |Canarês            |ಕನ್ನಡ                        |kn    |https://flagcdn.com/16x12/in.png    |
|South Korea                 |Korean             |Coreano            |한국어                          |ko    |https://flagcdn.com/16x12/kr.png    |
|India                       |Konkani            |Concâni            |कोंकणी                       |kok   |https://flagcdn.com/16x12/in.png    |
|Kurdistan                   |Kurdish            |Curdo              |Kurdî/کوردی                  |ku    |[Regional]                          |
|Kyrgyzstan                  |Kyrgyz             |Quirguiz           |Кыргыз                       |ky    |https://flagcdn.com/16x12/kg.png    |
|Luxembourg                  |Luxembourgish      |Luxemburguês       |Lëtzebuergesch               |lb    |https://flagcdn.com/16x12/lu.png    |
|Laos                        |Lao                |Laociano           |ລາວ                          |lo    |https://flagcdn.com/16x12/la.png    |
|Lithuania                   |Lithuanian         |Lituano            |lietuvių                     |lt    |https://flagcdn.com/16x12/lt.png    |
|Latvia                      |Latvian            |Letão              |latviešu                     |lv    |https://flagcdn.com/16x12/lv.png    |
|New Zealand                 |Maori              |Maori              |Reo Māori                    |mi    |https://flagcdn.com/16x12/nz.png    |
|Macedonia                   |Macedonian         |Macedônio          |македонски јазик             |mk    |https://flagcdn.com/16x12/mk.png    |
|India                       |Malayalam          |Malaiala           |മലയാളം                       |ml    |https://flagcdn.com/16x12/in.png    |
|Mongolia                    |Mongolian          |Mongol             |Монгол хэл/ᠮᠤᠨᠭᠭᠤᠯ ᠬᠡᠯᠡ      |mn    |https://flagcdn.com/16x12/mn.png    |
|Canada                      |Mohawk             |Mohawk             |Kanien'kéha                  |moh   |https://flagcdn.com/16x12/ca.png    |
|India                       |Marathi            |Marata             |मराठी                        |mr    |https://flagcdn.com/16x12/in.png    |
|Malaysia                    |Malay              |Malaio             |Bahasa Malaysia              |ms    |https://flagcdn.com/16x12/my.png    |
|Malta                       |Maltese            |Maltês             |Malti                        |mt    |https://flagcdn.com/16x12/mt.png    |
|Myanmar                     |Burmese            |Birmanês           |မြန်မာဘာသာ                   |my    |https://flagcdn.com/16x12/mm.png    |
|Norway                      |Norwegian (Bokmål) |Norueguês (Bokmål) |norsk (bokmål)               |nb    |https://flagcdn.com/16x12/no.png    |
|Nepal                       |Nepali             |Nepalês            |नेपाली (नेपाल)               |ne    |https://flagcdn.com/16x12/np.png    |
|Netherlands                 |Dutch              |Holandês           |Nederlands                   |nl    |https://flagcdn.com/16x12/nl.png    |
|Norway                      |Norwegian (Nynorsk)|Norueguês (Nynorsk)|norsk (nynorsk)              |nn    |https://flagcdn.com/16x12/no.png    |
|Norway                      |Norwegian          |Norueguês          |norsk                        |no    |https://flagcdn.com/16x12/no.png    |
|Occitania (France)          |Occitan            |Occitano           |occitan                      |oc    |https://flagcdn.com/16x12/fr.png    |
|India                       |Odia               |Oriá               |ଓଡ଼ିଆ                        |or    |https://flagcdn.com/16x12/in.png    |
|Netherlands Antilles        |Papiamento         |Papiamento         |Papiamentu                   |pap   |https://flagcdn.com/16x12/nl.png    |
|India/Pakistan              |Punjabi            |Punjabi            |ਪੰਜਾਬੀ/پنجابی                |pa    |https://flagcdn.com/16x12/in.png    |
|Poland                      |Polish             |Polonês            |polski                       |pl    |https://flagcdn.com/16x12/pl.png    |
|Afghanistan                 |Dari               |Dari               |درى                          |prs   |https://flagcdn.com/16x12/af.png    |
|Afghanistan                 |Pashto             |Pashto             |پښتو                         |ps    |https://flagcdn.com/16x12/af.png    |
|Portugal                    |Portuguese         |Português          |português                    |pt    |https://flagcdn.com/16x12/pt.png    |
|Guatemala                   |K'iche             |Quiché             |K'iche                       |quc   |https://flagcdn.com/16x12/gt.png    |
|Peru                        |Quechua            |Quíchua            |runasimi                     |qu    |https://flagcdn.com/16x12/pe.png    |
|Switzerland                 |Romansh            |Romanche           |Rumantsch                    |rm    |https://flagcdn.com/16x12/ch.png    |
|Romania                     |Romanian           |Romeno             |română                       |ro    |https://flagcdn.com/16x12/ro.png    |
|Russia                      |Russian            |Russo              |русский                      |ru    |https://flagcdn.com/16x12/ru.png    |
|Rwanda                      |Kinyarwanda        |Quiniaruanda       |Kinyarwanda                  |rw    |https://flagcdn.com/16x12/rw.png    |
|India                       |Sanskrit           |Sânscrito          |संस्कृत                      |sa    |https://flagcdn.com/16x12/in.png    |
|Russia                      |Yakut              |Iacuto             |саха                         |sah   |https://flagcdn.com/16x12/ru.png    |
|Sápmi (Norway)              |Sami (Northern)    |Sami (Norte)       |davvisámegiella              |se    |https://flagcdn.com/16x12/no.png    |
|Sri Lanka                   |Sinhala            |Cingalês           |සිංහල                        |si    |https://flagcdn.com/16x12/lk.png    |
|Slovakia                    |Slovak             |Eslovaco           |slovenčina                   |sk    |https://flagcdn.com/16x12/sk.png    |
|Slovenia                    |Slovenian          |Esloveno           |slovenski                    |sl    |https://flagcdn.com/16x12/si.png    |
|Sápmi (Sweden)              |Sami (Southern)    |Sami (Sul)         |åarjelsaemiengiele           |sma   |https://flagcdn.com/16x12/se.png    |
|Sápmi (Sweden)              |Sami (Lule)        |Sami (Lule)        |julevusámegiella             |smj   |https://flagcdn.com/16x12/se.png    |
|Finland                     |Sami (Inari)       |Sami (Inari)       |sämikielâ                    |smn   |https://flagcdn.com/16x12/fi.png    |
|Sápmi (Finland)             |Sami (Skolt)       |Sami (Skolt)       |sääʹmǩiõll                   |sms   |https://flagcdn.com/16x12/fi.png    |
|Albania                     |Albanian           |Albanês            |shqip                        |sq    |https://flagcdn.com/16x12/al.png    |
|Serbia                      |Serbian            |Sérvio             |srpski/српски                |sr    |https://flagcdn.com/16x12/rs.png    |
|Lesotho                     |Sesotho            |Sessoto            |Sesotho                      |st    |https://flagcdn.com/16x12/ls.png    |
|Sweden                      |Swedish            |Sueco              |svenska                      |sv    |https://flagcdn.com/16x12/se.png    |
|Tanzania                    |Kiswahili          |Suaíli             |Kiswahili                    |sw    |https://flagcdn.com/16x12/tz.png    |
|Syriac Christian communities|Syriac             |Siríaco            |ܣܘܪܝܝܐ                       |syc   |[Regional]                          |
|India                       |Tamil              |Tâmil              |தமிழ்                        |ta    |https://flagcdn.com/16x12/in.png    |
|India                       |Telugu             |Telugo             |తెలుగు                       |te    |https://flagcdn.com/16x12/in.png    |
|Tajikistan                  |Tajik              |Tadjique           |Тоҷикӣ                       |tg    |https://flagcdn.com/16x12/tj.png    |
|Thailand                    |Thai               |Tailandês          |ไทย                          |th    |https://flagcdn.com/16x12/th.png    |
|Turkmenistan                |Turkmen            |Turcomeno          |türkmençe                    |tk    |https://flagcdn.com/16x12/tm.png    |
|Botswana                    |Tswana             |Tswana             |Setswana                     |tn    |https://flagcdn.com/16x12/bw.png    |
|Turkey                      |Turkish            |Turco              |Türkçe                       |tr    |https://flagcdn.com/16x12/tr.png    |
|Tatarstan (Russia)          |Tatar              |Tártaro            |Татарча                      |tt    |https://flagcdn.com/16x12/ru.png    |
|Morocco                     |Tamazight          |Tamazigue          |Tamazight                    |tzm   |https://flagcdn.com/16x12/ma.png    |
|China                       |Uyghur             |Uigur              |ئۇيغۇرچە                     |ug    |https://flagcdn.com/16x12/cn.png    |
|Ukraine                     |Ukrainian          |Ucraniano          |українська                   |uk    |https://flagcdn.com/16x12/ua.png    |
|Pakistan                    |Urdu               |Urdu               |اُردو                        |ur    |https://flagcdn.com/16x12/pk.png    |
|Uzbekistan                  |Uzbek              |Usbeque            |Uzbek/Ўзбек                  |uz    |https://flagcdn.com/16x12/uz.png    |
|Vietnam                     |Vietnamese         |Vietnamita         |Tiếng Việt                   |vi    |https://flagcdn.com/16x12/vn.png    |
|Senegal                     |Wolof              |Wolof              |Wolof                        |wo    |https://flagcdn.com/16x12/sn.png    |
|South Africa                |Xhosa              |Xhosa              |isiXhosa                     |xh    |https://flagcdn.com/16x12/za.png    |
|Nigeria                     |Yoruba             |Iorubá             |Yoruba                       |yo    |https://flagcdn.com/16x12/ng.png    |
|China                       |Chinese            |Chinês             |中文                           |zh    |https://flagcdn.com/16x12/cn.png    |
|South Africa                |Zulu               |Zulu               |isiZulu                      |zu    |https://flagcdn.com/16x12/za.png    |



## Direct Links to Data and Schema

To access the language code tables and related schema, use the links below:

- **CSV Format Table**: [Download CSV Table](link_to_csv) or use direct in your program with http request to https://xxxx
- **JSON Format Table**: [Download JSON Table](link_to_json) or use direct in your program with http request to https://xxxx

- **JSON Schema**: [Download JSON Schema](link_to_json_schema) or use direct in your program with http request to https://xxxx


## Examples of Language Code Usage in Programming
### HTML
```html
<html lang="en">
```
### Javascript
```javascript
const userLanguage = navigator.language;
alert('Your language is: ' + userLanguage);
```
### Python
```python
import locale
current_locale = locale.getdefaultlocale()
print("Current locale is:", current_locale)
```
### Java
```java
import java.util.Locale;

public class Main {
    public static void main(String[] args) {
        Locale locale = new Locale("fr", "FR");
        System.out.println("Language: " + locale.getLanguage());
        System.out.println("Country: " + locale.getCountry());
    }
}
```

### .NET
```dotnet
using System.Globalization;
using System.Threading;

class Program {
    static void Main() {
        CultureInfo cultureInfo = new CultureInfo("es-ES");
        Thread.CurrentThread.CurrentCulture = cultureInfo;
        Thread.CurrentThread.CurrentUICulture = cultureInfo;
        
        Console.WriteLine("Current Culture: " + CultureInfo.CurrentCulture.Name);
    }
}
```
* .Net locale use (C# CultureInfo) name in format LanguageCode2[-Country/RegionCode2]. Please refer to link https://www.venea.net/web/culture-code to get .NET Culture related codes.


### Use in Google Speech API
```python
from google.cloud import translate

def translate_text(text="Hello, world!", target="fr"):
    client = translate.TranslationServiceClient()
    response = client.translate_text(
        contents=[text],
        target_language_code=target,
        parent="projects/your-project-id"
    )
    for translation in response.translations:
        print("Translated text: ", translation.translated_text)

translate_text()
```

## Licensing

This project is open-sourced under the MIT License.

## Reporting Issues

Please file an issue in the repository using the GitHub Issue Tracker if you encounter any problems.

## Contributing

Contributions are welcome! Please fork the repository and use a feature branch. Pull requests are warmly welcome. Please read XXX.md to Contribution Guide.

## Citation
If you use this repo please cite it in your **README.md** too.

### General citation
> Lopes, Flavio (2024). *Language Code Table*. Dados na Prática. This repository contains table of BCP 47 and RFC 4646 language tables and how to use it in programing languages. Available at: **Language Code Repository** https://github.com/dadosnapratica/language-code-table

### BlibTex citation
* For Academic or Cience articles
```bibtex
@misc{Lopes24LanguageCodeTable,
  author = {Flavio Lopes},
  title = {{Language Code Table}},
  year = {2024},
  publisher = {Dados na Pratica},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/dadosnapratica/language-code-table}},
  commit = {The commit ID if needed for more specific referencing},
  note = {Accessed: 2025-01-09}
}
```


## Utilization of AI in This Project

This content was partly created with the assistance of AI, specifically using ChatGPT, 4th generation.
  
If you want to see the prompt I used, see it at, share it:
[ChatGPT Prompt - Extract Language Code Tables](https://chatgpt.com/share/677f7883-9630-800d-958d-570e11be7b08)

## References

-   [Wikipedia IETF Language Tags Overview](https://en.wikipedia.org/wiki/IETF_language_tag) - An overview of IETF language tags, their purpose, structure, and usage.
-   [RFC BCP 47: Tags for Identifying Languages](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) - Best Current Practices for the tags used to identify languages.
-   [RFC 4646: Tags for Identifying Languages](https://datatracker.ietf.org/doc/html/rfc4646) - Details on the structure and rules for creating language tags for internet applications.
-   [Language Tags and Codes Explained by W3C](https://www.w3.org/International/articles/language-tags/) - How to construct language tags and their application in HTML and XML.
-   [Comprehensive List of Culture Codes](https://www.venea.net/web/culture-code) - A detailed list of culture names, ISO codes, Windows codes, and IETF language tags. Special usingn with .NET CultureInfo related langueage codes.

## Final Notes

This project was developed as an educational tool to demonstrate how Python can be used to analyze real data. It also explores how Artificial Intelligence can be integrated into analytical processes.

PIX is a digital payment system in Brazil that allows instant payments 24/7 via mobile phones. If you found this project helpful, please consider buying me a coffee. My PIX QR code is available in the repository.

![Coffee QR Code](qr_code_pix_bradesco.png)

## Author

**Flavio Lopes** Spreading practical data knowledge for decision making.

## Contact

Questions, suggestions, or improvements? Contact me or contribute directly to the repository.

-   **GitHub**: [dadosnapratica](https://github.com/orgs/dadosnapratica)
-   **LinkedIn**: [Flavio Lopes](https://www.linkedin.com/in/flavionlopes/)
-   **Email**: [flavio.lopes@ideiasfactory.tech](mailto:flavio.lopes@ideiasfactory.tech)
-   **Instagram**: [@dadosnapratica](https://www.instagram.com/dadosnapratica/)