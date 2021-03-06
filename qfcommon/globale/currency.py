#coding: utf-8
# ref: https://en.wikipedia.org/wiki/ISO_4217
#Currency = {
#    "156" : "CNY", # 人民币
#    "344" : "HKD", # 港元
#    "826" : "GBP", # 英镑
#    "840" : "USD", # 美元
#    "392" : "JPY", # 日元
#    "124" : "CAD", # 加拿大元
#    "554" : "NZD", # 新西兰
#    "410" : "KRW", # 韩国
#}
Currency = {
    '008': 'ALL',
    '012': 'DZD',
    '032': 'ARS',
    '036': 'AUD',
    '044': 'BSD',
    '048': 'BHD',
    '050': 'BDT',
    '051': 'AMD',
    '052': 'BBD',
    '060': 'BMD',
    '064': 'BTN',
    '068': 'BOB',
    '072': 'BWP',
    '084': 'BZD',
    '090': 'SBD',
    '096': 'BND',
    '104': 'MMK',
    '108': 'BIF',
    '116': 'KHR',
    '124': 'CAD',
    '132': 'CVE',
    '136': 'KYD',
    '144': 'LKR',
    '152': 'CLP',
    '156': 'CNY',
    '170': 'COP',
    '174': 'KMF',
    '188': 'CRC',
    '191': 'HRK',
    '192': 'CUP',
    '203': 'CZK',
    '208': 'DKK',
    '214': 'DOP',
    '222': 'SVC',
    '230': 'ETB',
    '232': 'ERN',
    '238': 'FKP',
    '242': 'FJD',
    '262': 'DJF',
    '270': 'GMD',
    '292': 'GIP',
    '320': 'GTQ',
    '324': 'GNF',
    '328': 'GYD',
    '332': 'HTG',
    '340': 'HNL',
    '344': 'HKD',
    '348': 'HUF',
    '352': 'ISK',
    '356': 'INR',
    '360': 'IDR',
    '364': 'IRR',
    '368': 'IQD',
    '376': 'ILS',
    '388': 'JMD',
    '392': 'JPY',
    '398': 'KZT',
    '400': 'JOD',
    '404': 'KES',
    '408': 'KPW',
    '410': 'KRW',
    '414': 'KWD',
    '417': 'KGS',
    '418': 'LAK',
    '422': 'LBP',
    '426': 'LSL',
    '430': 'LRD',
    '434': 'LYD',
    '446': 'MOP',
    '454': 'MWK',
    '458': 'MYR',
    '462': 'MVR',
    '478': 'MRO',
    '480': 'MUR',
    '484': 'MXN',
    '496': 'MNT',
    '498': 'MDL',
    '504': 'MAD',
    '512': 'OMR',
    '516': 'NAD',
    '524': 'NPR',
    '532': 'ANG',
    '533': 'AWG',
    '548': 'VUV',
    '554': 'NZD',
    '558': 'NIO',
    '566': 'NGN',
    '578': 'NOK',
    '586': 'PKR',
    '590': 'PAB',
    '598': 'PGK',
    '600': 'PYG',
    '604': 'PEN',
    '608': 'PHP',
    '634': 'QAR',
    '643': 'RUB',
    '646': 'RWF',
    '654': 'SHP',
    '678': 'STD',
    '682': 'SAR',
    '690': 'SCR',
    '694': 'SLL',
    '702': 'SGD',
    '704': 'VND',
    '706': 'SOS',
    '710': 'ZAR',
    '728': 'SSP',
    '748': 'SZL',
    '752': 'SEK',
    '756': 'CHF',
    '760': 'SYP',
    '764': 'THB',
    '776': 'TOP',
    '780': 'TTD',
    '784': 'AED',
    '788': 'TND',
    '800': 'UGX',
    '807': 'MKD',
    '818': 'EGP',
    '826': 'GBP',
    '834': 'TZS',
    '840': 'USD',
    '858': 'UYU',
    '860': 'UZS',
    '882': 'WST',
    '886': 'YER',
    '901': 'TWD',
    '931': 'CUC',
    '932': 'ZWL',
    '934': 'TMT',
    '936': 'GHS',
    '937': 'VEF',
    '938': 'SDG',
    '940': 'UYI',
    '941': 'RSD',
    '943': 'MZN',
    '944': 'AZN',
    '946': 'RON',
    '947': 'CHE',
    '948': 'CHW',
    '949': 'TRY',
    '950': 'XAF',
    '951': 'XCD',
    '952': 'XOF',
    '953': 'XPF',
    '955': 'XBA',
    '956': 'XBB',
    '957': 'XBC',
    '958': 'XBD',
    '959': 'XAU',
    '960': 'XDR',
    '961': 'XAG',
    '962': 'XPT',
    '963': 'XTS',
    '964': 'XPD',
    '965': 'XUA',
    '967': 'ZMW',
    '968': 'SRD',
    '969': 'MGA',
    '970': 'COU',
    '971': 'AFN',
    '972': 'TJS',
    '973': 'AOA',
    '974': 'BYR',
    '975': 'BGN',
    '976': 'CDF',
    '977': 'BAM',
    '978': 'EUR',
    '979': 'MXV',
    '980': 'UAH',
    '981': 'GEL',
    '984': 'BOV',
    '985': 'PLN',
    '986': 'BRL',
    '990': 'CLF',
    '994': 'XSU',
    '997': 'USN',
    '999': 'XXX',
}


Currency_name = {
    'AED':'阿拉伯联合酋长国迪尔汗／迪拉姆',
    'AFN':'阿富汗阿富汗尼（货币单位是“阿富汗尼”而不只是“尼”）',
    'ALL':'阿尔巴尼亚列克',
    'AMD':'亚美尼亚德拉姆',
    'AOA':'安哥拉宽扎',
    'ARS':'阿根廷比索',
    'AUD':'澳大利亚元（澳元）',
    'AWG':'阿鲁巴弗罗林／基尔德',
    'AZN':'阿塞拜疆马纳特',
    'BAM':'波斯尼亚和黑塞哥维那可兑换马克',
    'BBD':'巴巴多斯元',
    'BDT':'孟加拉塔卡',
    'BGN':'保加利亚列弗',
    'BHD':'巴林第纳尔',
    'BIF':'布隆迪法郎',
    'BMD':'百慕大元',
    'BND':'文莱元',
    'BOB':'玻利维亚玻利维亚诺（货币单位是“玻利维亚诺”而不只是“诺”）',
    'BOV':'玻利维亚 mvdol（资金）（基金）',
    'BRL':'巴西雷亚尔',
    'BSD':'巴哈马元',
    'BTN':'不丹努扎姆（也用印度卢比（INR））',
    'BWP':'博茨瓦纳普拉',
    'BYR':'白俄罗斯卢布',
    'BZD':'伯利兹元',
    'CAD':'加拿大元',
    'CDF':'刚果民主共和国刚果法郎',
    'CHF':'瑞士法郎',
    'CLF':'智利比索（可兑换的基金）',
    'CLP':'智利比索',
    'CNH':'中国人民币元〈离岸〉',
    'CNY':'人民币',
    'COP':'哥伦比亚比索',
    'COU':'哥伦比亚unidad de valor real',
    'CRC':'哥斯达黎加科朗',
    'CUC':'古巴可兑换比索',
    'CUP':'古巴比索',
    'CVE':'佛得角埃斯库多',
    'CZK':'捷克克朗',
    'DJF':'吉布提法郎',
    'DKK':'丹麦克朗',
    'DOP':'多米尼加比索',
    'DZD':'阿尔及利亚第纳尔',
    'EGP':'埃及镑',
    'ERN':'厄立特里亚纳克法',
    'ETB':'埃塞俄比亚比尔',
    'EUR':'欧元',
    'FJD':'斐济元',
    'FKP':'福克兰镑',
    'GBP':'英镑',
    'GEL':'格鲁吉亚拉里',
    'GHC':'加纳塞地',
    'GIP':'直布罗陀镑',
    'GMD':'冈比亚达拉西',
    'GNF':'几内亚法郎',
    'GTQ':'危地马拉格查尔',
    'GYD':'圭亚那元',
    'HKD':'港币',
    'HNL':'洪都拉斯伦皮拉',
    'HRK':'克罗地亚库纳',
    'HTG':'海地古德',
    'HUF':'匈牙利 福林（又称富林，见CNS 12873）',
    'IDR':'印度尼西亚盾／卢比',
    'ILS':'以色列新谢克尔',
    'INR':'印度卢比',
    'IQD':'伊拉克第纳尔',
    'IRR':'伊朗里亚尔',
    'ISK':'冰岛克朗',
    'JMD':'牙买加元',
    'JOD':'约旦第纳尔',
    'JPY':'日本日圆',
    'KES':'肯尼亚先令',
    'KGS':'吉尔吉斯斯坦索姆',
    'KHR':'柬埔寨瑞尔（台湾也作里耳）',
    'KMF':'科摩罗法郎',
    'KPW':'朝鲜朝鲜圆',
    'KRW':'韩国韩圆',
    'KWD':'科威特第纳尔',
    'KYD':'开曼元',
    'KZT':'哈萨克坦吉',
    'LAK':'老挝基普',
    'LBP':'黎巴嫩镑',
    'LKR':'斯里兰卡卢比',
    'LRD':'利比里亚元',
    'LSL':'莱索托洛蒂（复数：马洛蒂）',
    'LTL':'立陶宛立特',
    'LYD':'利比亚第纳尔',
    'MAD':'摩洛哥迪拉姆',
    'MDL':'摩尔多瓦列伊／摩列伊',
    'MGA':'马达加斯加阿里亚里',
    'MKD':'前南马其顿代纳尔',
    'MMK':'缅元',
    'MNT':'蒙古图格里克',
    'MOP':'澳门币',
    'MRO':'毛里塔尼亚乌吉亚',
    'MUR':'毛里求斯卢比',
    'MVR':'马尔代夫拉菲亚',
    'MWK':'马拉维克瓦查',
    'MXN':'墨西哥比索',
    'MXV':'墨西哥Unidad de Inversion (UDI)（资金）（基金）',
    'MYR':'马来西亚令吉（马来西亚译名）；林吉特（中华民国和中华人民共和国国家标准译名，但不符马来语读音）',
    'MZN':'莫桑比克梅蒂卡尔',
    'NAD':'纳米比亚元（也用南非兰特（ZAR））',
    'NGN':'尼日利亚奈拉',
    'NIO':'尼加拉瓜科多巴',
    'NOK':'挪威克朗',
    'NPR':'尼泊尔卢比',
    'NZD':'新西兰元（纽元）',
    'OMR':'阿曼里亚尔',
    'PAB':'巴拿马巴波亚（也用美元（USD））',
    'PEN':'秘鲁新索尔',
    'PGK':'巴布亚新几内亚基那',
    'PHP':'菲律宾比索',
    'PKR':'巴基斯坦卢比',
    'PLN':'波兰兹罗提',
    'PYG':'巴拉圭瓜拉尼',
    'QAR':'卡塔尔里亚尔',
    'RON':'罗马尼亚列伊（台湾也作罗依）',
    'RSD':'塞尔维亚第纳尔',
    'RUB':'俄罗斯卢布',
    'RWF':'卢旺达法郎',
    'SAR':'沙特里亚尔',
    'SBD':'所罗门群岛元',
    'SCR':'塞舌尔卢比',
    'SDG':'苏丹苏丹镑',
    'SEK':'瑞典克朗',
    'SGD':'新加坡元',
    'SHP':'圣赫勒拿镑',
    'SLL':'塞拉利昂利昂',
    'SOS':'索马里先令',
    'SRD':'苏里南元',
    'SSP':'南苏丹南苏丹镑',
    'STD':'圣多美和普林西比多布拉',
    'SYP':'叙利亚镑',
    'SZL':'斯威士兰里兰吉尼（复数：埃马兰吉尼 emalangeni）',
    'THB':'泰铢',
    'TJS':'塔吉克斯坦索莫尼',
    'TMT':'土库曼斯坦马纳特',
    'TND':'突尼斯第纳尔',
    'TOP':'汤加潘加',
    'TRY':'新土耳其里拉',
    'TTD':'特立尼达和多巴哥元',
    'TWD':'新台币元',
    'TZS':'坦桑尼亚先令',
    'UAH':'乌克兰赫里夫尼亚／格里夫纳',
    'UGX':'乌干达先令',
    'USD':'美元',
    'USN':'美元（次日）（资金）（第二天）（基金）',
    'USS':'美元（当日）（资金）（同一天）（基金）',
    'UYI':'乌拉圭Uruguay Peso en Unidades Indexadas',
    'UYU':'乌拉圭比索',
    'UZS':'乌兹别克斯坦苏姆',
    'VEF':'委内瑞拉玻利瓦尔',
    'VND':'越南盾',
    'VUV':'瓦努阿图瓦图',
    'WST':'萨摩亚塔拉',
    'XAF':'中非金融合作法郎（中非法郎）',
    'XAG':'银',
    'XAU':'金',
    'XBA':'欧洲复合单位 (EURCO)／欧洲混合单位（债券市场单位）',
    'XBB':'欧洲货币联盟 (E.M.U.-6)（债券市场单位）',
    'XBC':'9号账户的欧洲单位（债券市场单位）',
    'XBD':'17号账户的欧洲单位（债券市场单位）',
    'XCD':'汤加勒比元',
    'XDR':'特别提款权（国际货币基金）',
    'XFU':'UIC-法郎（特殊协定货币）',
    'XOF':'非洲金融共同体法郎（西非法郎）',
    'XPD':'钯',
    'XPF':'太平洋法郎（CFP法郎）',
    'XPT':'铂',
    'XTS':'为测试保留的代码',
    'XXX':'没有货币的交换',
    'YER':'也门里亚尔',
    'ZAR':'南非兰特',
    'ZMW':'赞比亚克瓦查',
}

Currency_symbol = {
    '344' : '$' , 
    '901' : '$' ,
    '978' : '€' ,
    '840' : '$' ,
    '826' : '£' ,
    '036' : '$' ,
    '410' : '₩' ,
    '392' : '¥' ,
    '124' : '$' ,
    '554' : '$' ,
    '764' : '฿' ,
    '702' : '$' ,
    '156' : '￥',
}
