
# coding: utf-8

# In[ ]:


# Библиотека присвоения порядкового номера монете


# In[5]:


CoinDictonary = {
"Bitcoin": '1',
"Ethereum": '2',
"Ripple": '3',
"Bitcoin Cash": '4',
"Cardano": '5',
"Stellar": '6',
"Litecoin": '7',
"EOS": '8',
"NEO": '9',
"NEM": '10',
"IOTA": '11',
"Dash": '12',
"Monero": '13',
"TRON": '14',
"VeChain": '15',
"Bitcoin Gold": '16',
"ICON": '17',
"Qtum": '18',
"Ethereum Classic": '19',
"Lisk": '20',
"RaiBlocks": '21',
"Populous": '22',
"OmiseGO": '23',
"Tether": '24',
"Steem": '25',
"Stratis": '26',
"Zcash": '27',
"Bytecoin": '28',
"Binance Coin": '29',
"Verge": '30',
"BitShares": '31',
"Siacoin": '32',
"0x": '33',
"Status": '34',
"Ardor": '35',
"Walton": '36',
"Waves": '37',
"Augur": '38',
"Maker": '39',
"Dogecoin": '40',
"KuCoin Shares": '41',
"Veritaseum": '42',
"Hshare": '43',
"Komodo": '44',
"Ark": '45',
"Electroneum": '46',
"RChain": '47',
"Loopring": '48',
"Dragonchain": '49',
"IOStoken": '50',
"Decred": '51',
"Aeternity": '52',
"Basic Attention Token": '53',
"DigiByte": '54',
"Dentacoin": '55',
"PIVX": '56',
"Kyber Network": '57',
"aelf": '58',
"QASH": '59',
"DigixDAO": '60',
"Gas": '61',
"ZClassic": '62',
"Byteball Bytes": '63',
"Golem": '64',
"WAX": '65',
"FunFair": '66',
"Bytom": '67',
"Cindicator": '68',
"SALT": '69',
"Ethos": '70',
"Nebulas": '71',
"Factom": '72',
"Cryptonex": '73',
"SmartCash": '74',
"Aion": '75',
"Power Ledger": '76',
"Dent": '77',
"Syscoin": '78',
"Nexus": '79',
"ReddCoin": '80',
"GXShares": '81',
"MonaCoin": '82',
"Nxt": '83',
"MaidSafeCoin": '84',
"Enigma": '85',
"MediBloc": '86',
"ZCoin": '87',
"SIRIN LABS Token": '88',
"Bancor": '89',
"Request Network": '90',
"Particl": '91',
"Bitcore": '92',
"GameCredits": '93',
"Substratum": '94',
"Experience Points": '95',
"Kin": '96',
"Quantstamp": '97',
"Storm": '98',
"Iconomi": '99',
"Neblio": '100',
"TenX": '101',
"Pillar": '102',
"ChainLink": '103',
"Gnosis": '104',
"Civic": '105',
"iExec RLC": '106',
"Emercoin": '107',
"DigitalNote": '108',
"Raiden Network Token": '109',
"Po.et": '110',
"SophiaTX": '111',
"XPlay": '112',
"Time New Bank": '113',
"Skycoin": '114',
"Enjin Coin": '115',
"DEW": '116',
"Storj": '117',
"Vertcoin": '118',
"BitcoinDark": '119',
"Aragon": '120',
"BridgeCoin": '121',
"AirSwap": '122',
"Achain": '123',
"Ubiq": '124',
"PACcoin": '125',
"Cobinhood": '126',
"BLOCKv": '127',
"Blocknet": '128',
"SuperNET": '129',
"SingularDTV": '130',
"ETHLend": '131',
"Santiment Network Token": '132',
"PayPie": '133',
"NAV Coin": '134',
"VIBE": '135',
"Theta Token": '136',
"Ripio Credit Network": '137',
"Red Pulse": '138',
"Monaco": '139',
"Simple Token": '140',
"DeepBrain Chain": '141',
"Dynamic Trading Rights": '142',
"Ambrosus": '143',
"Telcoin": '144',
"Decentraland": '145',
"High Performance Blockchain": '146',
"HTMLCOIN": '147',
"BitBay": '148',
"Counterparty": '149',
"AppCoins": '150',
"Asch": '151',
"XTRABYTES": '152',
"INS Ecosystem": '153',
"ZenCash": '154',
"Einsteinium": '155',
"Revain": '156',
"Bibox Token": '157',
"Unikoin Gold": '158',
"Centra": '159',
"Peercoin": '160',
"adToken": '161',
"WaBi": '162',
"Agoras Tokens": '163',
"AdEx": '164',
"SONM": '165',
"IoT Chain": '166',
"Metaverse ETP": '167',
"SpankChain": '168',
"CyberMiles": '169',
"MediShares": '170',
"Edgeless": '171',
"Internet Node Token": '172',
"Nuls": '173',
"ION": '174',
"Modum": '175',
"Streamr DATAcoin": '176',
"Tierion": '177',
"Quantum Resistant Ledger": '178',
"Melon": '179',
"Bread": '180',
"BitConnect": '181',
"Etherparty": '182',
"ATMChain": '183',
"Gulden": '184',
"CoinDash": '185',
"district0x": '186',
"Electra": '187',
"Metal": '188',
"LBRY Credits": '189',
"Wings": '190',
"UTRUST": '191',
"ECC": '192',
"Trinity Network Credit": '193',
"Viacoin": '194',
"QLINK": '195',
"DECENT": '196',
"Wagerr": '197',
"Rise": '198',
"Burst": '199',
"Oyster": '200',
"CloakCoin": '201',
"NAGA": '202',
"Decision Token": '203',
"FirstBlood": '204',
"Cappasity": '205',
"Triggers": '206',
"Aeon": '207',
"Lunyr": '208',
"Eidoo": '209',
"MobileGo": '210',
"Gifto": '211',
"Ink": '212',
"BitDegree": '213',
"Genesis Vision": '214',
"SaluS": '215',
"Lykke": '216',
"Grid+": '217',
"WeTrust": '218',
"HempCoin": '219',
"I/O Coin": '220',
"Groestlcoin": '221',
"TokenCard": '222',
"Lamden": '223',
"Selfkey": '224',
"Mercury": '225',
"Agrello": '226',
"TaaS": '227',
"Hive": '228',
"Voxels": '229',
"Cofound.it": '230',
"Shift": '231',
"COSS": '232',
"Spectrecoin": '233',
"Spectre.ai Dividend Token": '234',
"Datum": '235',
"bitCNY": '236',
"Delphy": '237',
"Pura": '238',
"Crown": '239',
"Everex": '240',
"iXledger": '241',
"MinexCoin": '242',
"Propy": '243',
"Dimecoin": '244',
"Paypex": '245',
"VeriCoin": '246',
"Blocktix": '247',
"Trade Token": '248',
"Bloom": '249',
"Namecoin": '250',
"EncrypGen": '251',
"Mooncoin": '252',
"Worldcore": '253',
"YOYOW": '254',
"Presearch": '255',
"Viberate": '256',
"Nimiq": '257',
"BitClave": '258',
"Feathercoin": '259',
"PotCoin": '260',
"Humaniq": '261',
"Steem Dollars": '262',
"Monetha": '263',
"Pepe Cash": '264',
"Mothership": '265',
"Safe Exchange Coin": '266',
"HelloGold": '267',
"Diamond": '268',
"Flash": '269',
"Jinn": '270',
"SIBCoin": '271',
"Zeusshield": '272',
"Game.com": '273',
"Elastic": '274',
"CanYaCoin": '275',
"LAToken": '276',
"Synereo": '277',
"Pascal Coin": '278',
"WhiteCoin": '279',
"Matchpool": '280',
"Moeda Loyalty Points": '281',
"Neumark": '282',
"FairCoin": '283',
"NuShares": '284',
"Bounty0x": '285',
"BlockMason Credit Protocol": '286',
"Aurora DAO": '287',
"BlackCoin": '288',
"SHIELD": '289',
"PoSW Coin": '290',
"Snovio": '291',
"NoLimitCoin": '292',
"Karma": '293',
"DomRaider": '294',
"DeepOnion": '295',
"GridCoin": '296',
"SolarCoin": '297',
"Peerplays": '298',
"SunContract": '299',
"Bodhi": '300',
"Golos": '301',
"Gambit": '302',
"Stox": '303',
"Expanse": '304',
"Aeron": '305',
"Covesting": '306',
"Ormeus Coin": '307',
"Numeraire": '308',
"Swarm City": '309',
"Phore": '310',
"Radium": '311',
"Voise": '312',
"Omni": '313',
"Hush": '314',
"Rivetz": '315',
"Xenon": '316',
"Myriad": '317',
"Boolberry": '318',
"Primas": '319',
"OKCash": '320',
"NVO": '321',
"OAX": '322',
"eBitcoin": '323',
"MonetaryUnit": '324',
"Divi": '325',
"Target Coin": '326',
"AirToken": '327',
"GET Protocol": '328',
"NeosCoin": '329',
"Blackmoon": '330',
"Bean Cash": '331',
"Playkey": '332',
"InvestFeed": '333',
"LEOcoin": '334',
"E-coin": '335',
"Regalcoin": '336',
"Rubycoin": '337',
"Nexium": '338',
"Maecenas": '339',
"LIFE": '340',
"Open Trading Network": '341',
"Paragon": '342',
"ColossusCoinXT": '343',
"Zoin": '344',
"BitSend": '345',
"Credo": '346',
"Pandacoin": '347',
"Patientory": '348',
"Hedge": '349',
"NewYorkCoin": '350',
"MyBit Token": '351',
"Unobtanium": '352',
"DubaiCoin": '353',
"Waves Community Token": '354',
"Databits": '355',
"LUXCoin": '356',
"ALIS": '357',
"KickCoin": '358',
"BitDice": '359',
"Mintcoin": '360',
"QunQun": '361',
"Primecoin": '362',
"Aventus": '363',
"BCAP": '364',
"Energycoin": '365',
"Elixir": '366',
"Incent": '367',
"FlorinCoin": '368',
"Soarcoin": '369',
"OracleChain": '370',
"Bismuth": '371',
"ICOS": '372',
"OneRoot Network": '373',
"Clams": '374',
"LoMoCoin": '375',
"Obsidian": '376',
"DecentBet": '377',
"Rialto": '378',
"Neutron": '379',
"Linda": '380',
"Polybius": '381',
"Aigang": '382',
"FoldingCoin": '383',
"Block Array": '384',
"ATBCoin": '385',
"Chronobank": '386',
"Universal Currency": '387',
"BLUE": '388',
"Publica": '389',
"ProChain": '390',
"ClearPoll": '391',
"Etheroll": '392',
"bitUSD": '393',
"Oxycoin": '394',
"SportyFi": '395',
"Sequence": '396',
"LendConnect": '397',
"Blockport": '398',
"CVCoin": '399',
"Musicoin": '400',
"Circuits of Value": '401',
"HEAT": '402',
"Bitcrystals": '403',
"Pirl": '404',
"Syndicate": '405',
"Change": '406',
"Global Currency Reserve": '407',
"Monoeci": '408',
"Dovu": '409',
"Uquid Coin": '410',
"Solaris": '411',
"BlockCAT": '412',
"Espers": '413',
"Internet of People": '414',
"Stealthcoin": '415',
"ArtByte": '416',
"Sphere": '417',
"OBITS": '418',
"GoByte": '419',
"DAO.Casino": '420',
"Xaurum": '421',
"LockChain": '422',
"Flixxo": '423',
"Payfair": '424',
"B2B": '425',
"Quantum": '426',
"Vsync": '427',
"Mysterium": '428',
"Verify": '429',
"bitqy": '430',
"Lampix": '431',
"Pluton": '432',
"PinkCoin": '433',
"Curecoin": '434',
"KiloCoin": '435',
"ALQO": '436',
"Leverj": '437',
"Exchange Union": '438',
"Sumokoin": '439',
"Polis": '440',
"Ethorse": '441',
"Auroracoin": '442',
"Spectre.ai Utility Token": '443',
"AsiaCoin": '444',
"Sprouts": '445',
"Russian Miner Coin": '446',
"SpreadCoin": '447',
"Autonio": '448',
"Devery": '449',
"E-Dinar Coin": '450',
"Bulwark": '451',
"Astro": '452',
"MyWish": '453',
"DopeCoin": '454',
"onG.social": '455',
"ProCurrency": '456',
"Hacken": '457',
"AdShares": '458',
"EarthCoin": '459',
"Atmos": '460',
"Wild Crypto": '461',
"FedoraCoin": '462',
"Bitdeal": '463',
"Vcash": '464',
"AudioCoin": '465',
"FlypMe": '466',
"FirstCoin": '467',
"TIES Network": '468',
"Social Send": '469',
"Innova": '470',
"Memetic / PepeCoin": '471',
"TrezarCoin": '472',
"TransferCoin": '473',
"Mercury Protocol": '474',
"Bitcloud": '475',
"VeriumReserve": '476',
"Hubii Network": '477',
"CrowdCoin": '478',
"HyperStake": '479',
"The ChampCoin": '480',
"Bela": '481',
"REX": '482',
"Ecobit": '483',
"RussiaCoin": '484',
"Breakout": '485',
"PRIZM": '486',
"Blitzcash": '487',
"CannabisCoin": '488',
"DigiPulse": '489',
"DCORP": '490',
"Qwark": '491',
"BuzzCoin": '492',
"Synergy": '493',
"Kore": '494',
"Upfiring": '495',
"ATLANT": '496',
"Bitmark": '497',
"Pesetacoin": '498',
"Creditbit": '499',
"1337": '500',
"IntenseCoin": '501',
"Dotcoin": '502',
"Opus": '503',
"Qvolta": '504',
"GoldCoin": '505',
"HEROcoin": '506',
"Bonpay": '507',
"Novacoin": '508',
"Bitcoin Plus": '509',
"Social": '510',
"MicroMoney": '511',
"BitcoinZ": '512',
"XGOX": '513',
"Altcoin": '514',
"Masternodecoin": '515',
"UFO Coin": '516',
"NuBits": '517',
"Riecoin": '518',
"Dai": '519',
"ToaCoin": '520',
"Breakout Stake": '521',
"ExclusiveCoin": '522',
"VIVO": '523',
"Interstellar Holdings": '524',
"TrueFlip": '525',
"Bitzeny": '526',
"Sharechain": '527',
"CHIPS": '528',
"Blockpool": '529',
"EuropeCoin": '530',
"2GIVE": '531',
"Rupee": '532',
"vTorrent": '533',
"REAL": '534',
"IncaKoin": '535',
"HollyWoodCoin": '536',
"Project Decorum": '537',
"Indorse Token": '538',
"Sexcoin": '539',
"ChainCoin": '540',
"Bowhead": '541',
"DNotes": '542',
"Tokes": '543',
"Eroscoin": '544',
"ZrCoin": '545',
"Startcoin": '546',
"Zero": '547',
"BitBoost": '548',
"TrustPlus": '549',
"Cryptopay": '550',
"Magnet": '551',
"Global Jobcoin": '552',
"Dynamic": '553',
"Creativecoin": '554',
"Internxt": '555',
"Zephyr": '556',
"Privatix": '557',
"WandX": '558',
"Karbo": '559',
"EncryptoTel [WAVES]": '560',
"PutinCoin": '561',
"Pylon Network": '562',
"Adelphoi": '563',
"Starta": '564',
"Ergo": '565',
"NobleCoin": '566',
"Magi": '567',
"Terracoin": '568',
"SmartBillions": '569',
"FLiK": '570',
"EverGreenCoin": '571',
"MCAP": '572',
"Farad": '573',
"NEVERDIE": '574',
"Pure": '575',
"Monkey Project": '576',
"Ethbits": '577',
"eBoost": '578',
"e-Gulden": '579',
"Zeitcoin": '580',
"MarteXcoin": '581',
"SmileyCoin": '582',
"STRAKS": '583',
"vSlice": '584',
"FORCE": '585',
"ELTCOIN": '586',
"Anoncoin": '587',
"Goodomy": '588',
"HunterCoin": '589',
"Ellaism": '590',
"Denarius": '591',
"CryptoPing": '592',
"BlueCoin": '593',
"bitJob": '594',
"ParkByte": '595',
"Quark": '596',
"APX": '597',
"Embers": '598',
"GCN Coin": '599',
"TheGCCcoin": '600',
"Carboncoin": '601',
"Ixcoin": '602',
"Yocoin": '603',
"OP Coin": '604',
"EquiTrader": '605',
"Dinastycoin": '606',
"ERC20": '607',
"Emphy": '608',
"Centurion": '609',
"Condensate": '610',
"Primalbase Token": '611',
"Moin": '612',
"Qbic": '613',
"Footy Cash": '614',
"Adzcoin": '615',
"Intelligent Trading Tech": '616',
"LiteDoge": '617',
"LuckChain": '618',
"Accelerator Network": '619',
"DigitalPrice": '620',
"Elementrem": '621',
"UnbreakableCoin": '622',
"Crypto Bullion": '623',
"Commodity Ad Network": '624',
"Unitus": '625',
"Greencoin": '626',
"FundYourselfNow": '627',
"Etheriya": '628',
"ICO OpenLedger": '629',
"DraftCoin": '630',
"Tracto": '631',
"LeviarCoin": '632',
"Linx": '633',
"Kubera Coin": '634',
"Gimli": '635',
"Oceanlab": '636',

"PopularCoin": '637',
"CampusCoin": '638',
"Canada eCoin": '639',
"ArcticCoin": '640',
"Unify": '641',
"Copico": '642',
"FujiCoin": '643',
"Bitradio": '644',
"Royal Kingdom Coin": '645',
"Scorecoin": '646',
"Darcrus": '647',
"Version": '648',
"WorldCoin": '649',
"Renos": '650',
"CarTaxi Token": '651',
"FlutterCoin": '652',
"Fastcoin": '653',
"Megacoin": '654',
"Desire": '655',
"NetCoin": '656',
"TeslaCoin": '657',
"Abjcoin": '658',
"42-coin": '659',
"InsaneCoin": '660',
"Bytecent": '661',
"Jetcoin": '662',
"InflationCoin": '663',
"FuckToken": '664',
"Bata": '665',
"CryptoForecast": '666',
"Skeincoin": '667',
"Ethereum Cash": '668',
"Bitcoin Scrypt": '669',
"MazaCoin": '670',
"Legends Room": '671',
"Cryptonite": '672',
"Influxcoin": '673',
"Confido": '674',
"AurumCoin": '675',
"Kolion": '676',
"PiplCoin": '677',
"Digitalcoin": '678',
"HitCoin": '679',
"Halcyon": '680',
"Steneum Coin": '681',
"TittieCoin": '682',
"Cryptojacks": '683',
"Bitpark Coin": '684',
"Link Platform": '685',
"BunnyCoin": '686',
"SkinCoin": '687',
"KekCoin": '688',
"CryptoCarbon": '689',
"Growers International": '690',
"eBitcoinCash": '691',
"MACRON": '692',
"PureVidz": '693',
"Zennies": '694',
"LanaCoin": '695',
"EthBet": '696',
"Piggycoin": '697',
"Miners' Reward Token": '698',
"BlakeStar": '699',
"Zetacoin": '700',
"Eternity": '701',
"Guncoin": '702',
"DROXNE": '703',
"UltraCoin": '704',
"GAIA": '705',
"I0Coin": '706',
"Ace": '707',
"BitBar": '708',
"HOdlcoin": '709',
"Kobocoin": '710',
"Authorship": '711',
"Cream": '712',
"Minereum": '713',
"Suretly": '714',
"QubitCoin": '715',
"ShadowCash": '716',
"SmartCoin": '717',
"Capricoin": '718',
"Deutsche eMark": '719',
"Bitstar": '720',
"iTicoin": '721',
"BigUp": '722',
"SagaCoin": '723',
"Machinecoin": '724',
"Netko": '725',
"AltCommunity Coin": '726',
"Visio": '727',
"Universe": '728',
"Rimbit": '729',
"Billionaire Token": '730',
"Octanox": '731',
"FUNCoin": '732',
"HoboNickels": '733',
"Bitcurrency": '734',
"FuelCoin": '735',
"Trollcoin": '736',
"Newbium": '737',
"Kurrent": '738',
"PetroDollar": '739',
"Ethereum Gold": '740',
"Atomic Coin": '741',
"WavesGo": '742',
"Titcoin": '743',
"DFSCoin": '744',
"DaxxCoin": '745',
"CoinonatX": '746',
"Nyancoin": '747',
"Bitcoin Red": '748',
"Joulecoin": '749',
"Blakecoin": '750',
"UniCoin": '751',
"Aricoin": '752',
"OctoCoin": '753',
"iEthereum": '754',
"RouletteToken": '755',
"Eryllium": '756',
"BiblePay": '757',
"808Coin": '758',
"GoldBlocks": '759',
"TrumpCoin": '760',
"PlatinumBAR": '761',
"Opal": '762',
"Bit20": '763',
"CryptoInsight": '764',
"SwagBucks": '765',
"AmsterdamCoin": '766',
"Madcoin": '767',
"Triangles": '768',
"Fujinto": '769',
"Happycoin": '770',
"Giga Watt Token": '771',
"AdCoin": '772',
"SuperCoin": '773',
"Coin(O)": '774',
"BlockPay": '775',
"PoSToken": '776',
"Ammo Reloaded": '777',
"DigiCube": '778',
"LiteBar": '779',
"Senderon": '780',
"Pakcoin": '781',
"Dashcoin": '782',
"Crave": '783',
"Nekonium": '784',
"Signatum": '785',
"Truckcoin": '786',
"Flycoin": '787',
"Sugar Exchange": '788',
"MojoCoin": '789',
"HiCoin": '790',
"WhaleCoin": '791',
"C-Bit": '792',
"Veltor": '793',
"Zlancer": '794',
"Elcoin": '795',
"Chronos": '796',
"Grimcoin": '797',
"Pioneer Coin": '798',
"Crystal Clear ": '799',
"PayCoin": '800',
"Xios": '801',
"Sterlingcoin": '802',
"DigitalDevelopersFund": '803',
"RevolverCoin": '804',
"Phoenixcoin": '805',
"Ethereum Dark": '806',
"Hawala.Today": '807',
"Sovereign Hero": '808',
"Tigercoin": '809',
"Onix": '810',
"iCoin": '811',
"ZoZoCoin": '812',
"PostCoin": '813',
"Evil Coin": '814',
"RedCoin": '815',
"Bolivarcoin": '816',
"ChessCoin": '817',
"Gapcoin": '818',
"StarCash Network": '819',
"Helleniccoin": '820',
"Bitcoin Fast": '821',
"BitTokens": '822',
"Mineum": '823',
"Coin2.1": '824',
"EOT Token": '825',
"Ccore": '826',
"Emerald Crypto": '827',
"BERNcash": '828',
"GoldReserve": '829',
"Swing": '830',
"SoonCoin": '831',
"LiteBitcoin": '832',
"ChanCoin": '833',
"TagCoin": '834',
"Litecoin Plus": '835',
"Unity Ingot": '836',
"TEKcoin": '837',
"CannaCoin": '838',
"Motocoin": '839',
"AquariusCoin": '840',
"Dix Asset": '841',
"Philosopher Stones": '842',
"bitBTC": '843',
"Quatloo": '844',
"Ratecoin": '845',
"Argentum": '846',
"YENTEN": '847',
"ParallelCoin": '848',
"SpaceCoin": '849',
"Hexx": '850',
"Catcoin": '851',
"VirtualCoin": '852',
"Marscoin": '853',
"Kayicoin": '854',
"Bitgem": '855',
"BumbaCoin": '856',
"Network Token": '857',
"MustangCoin": '858',
"LeaCoin": '859',
"Dalecoin": '860',
"GlobalBoost-Y": '861',
"BitCoal": '862',
"GameUnits": '863',
"Prime-XI": '864',
"Sativacoin": '865',
"VoteCoin": '866',
"BROTHER": '867',
"SixEleven": '868',
"Beatcoin": '869',
"ICOBID": '870',
"Darsek": '871',
"Independent Money System": '872',
"QuazarCoin": '873',
"Trident Group": '874',
"BitQuark": '875',
"PayCon": '876',
"Virtacoinplus": '877',
"SecureCoin": '878',
"bitGold": '879',
"BriaCoin": '880',
"Honey": '881',
"RonPaulCoin": '882',
"bitSilver": '883',
"Zurcoin": '884',
"Cypher": '885',
"FuzzBalls": '886',
"Advanced Internet Blocks": '887',
"Cashcoin": '888',
"CacheCoin": '889',
"NevaCoin": '890',
"Evotion": '891',
"ReeCoin": '892',
"GPU Coin": '893',
"BitAsean": '894',
"CompuCoin": '895',
"Yellow Token": '896',
"Eurocoin": '897',
"Gold Pressed Latinum": '898',
"Cannation": '899',
"GlobalToken": '900',
"Creatio": '901',
"Coinonat": '902',
"Marijuanacoin": '903',
"X-Coin": '904',
"Acoin": '905',
"SOILcoin": '906',
"SongCoin": '907',
"GoldPieces": '908',
"Digital Rupees": '909',
"Flaxscript": '910',
"Kronecoin": '911',
"Money": '912',
"BipCoin": '913',
"Rupaya": '914',
"EcoCoin": '915',
"DIBCOIN": '916',
"Allion": '917',
"VapersCoin": '918',
"Solarflarecoin": '919',
"Bolenum": '920',
"300 Token": '921',
"Theresa May Coin": '922',
"Neuro": '923',
"Cthulhu Offerings": '924',
"EagleCoin": '925',
"AllSafe": '926',
"CoExistCoin": '927',
"Comet": '928',
"BenjiRolls": '929',
"Spots": '930',
"BnrtxCoin": '931',
"Sojourn": '932',
"LiteCoin Ultra": '933',
"Torcoin": '934',
"Artex Coin": '935',
"Luna Coin": '936',
"Tychocoin": '937',
"HempCoin": '938',
"BOAT": '939',
"Master Swiscoin": '940',
"Iconic": '941',
"bitEUR": '942',
"WomenCoin": '943',
"Printerium": '944',
"PlayerCoin": '945',
"Roofs": '946',
"ExchangeN": '947',
"Speedcash": '948',
"Aerium": '949',
"Useless Ethereum Token": '950',
"Slevin": '951',
"KingN Coin": '952',
"MiloCoin": '953',
"GeertCoin": '954',
"Cabbage": '955',
"Dollar Online": '956',
"PRCoin": '957',
"Steps": '958',
"AnarchistsPrime": '959',
"CybCSec": '960',
"SocialCoin": '961',
"Credence Coin": '962',
"Shilling": '963',
"Coimatic 2.0": '964',
"Veros": '965',
"G3N": '966',
"BioBar": '967',
"Coimatic 3.0": '968',
"Argus": '969',
"Coupecoin": '970',
"Elysium": '971',
"AgrolifeCoin": '972',
"Project-X": '973',
"Vault Coin": '974',
"Bitvolt": '975',
"LevoPlus": '976',
"CrevaCoin": '977',
"Rawcoin": '978',
"Magnum": '979',
"Ulatech": '980',
"Concoin": '981',
"FuturXe": '982',
"EXRNchain": '983',
"Tristar Coin": '984',
"CaliphCoin": '985',
"HarmonyCoin": '986',
"Digital Credits": '987',
"Abncoin": '988',
"Ebittree Coin": '989',
"Digital Money Bits": '990',
"AppleCoin": '991',
"GeoCoin": '992',
"Virtacoin": '993',
"Prospectors Gold": '994',
"Tao": '995',
"Ethereum Movie Venture": '996',
"Rustbits": '997',
"CryptCoin": '998',
"Monster Byte": '999',
"Smart Investment Fund Token": '1000',
"Ultimate Secure Cash": '1001',
"Janus": '1002',
"InPay": '1003',
"StarCredits": '1004',
"CorgiCoin": '1005',
"Woodcoin": '1006',
"Shorty": '1007',
"Orbitcoin": '1008',
"YashCoin": '1009',
"Fantomcoin": '1010',
"BritCoin": '1011',
"MaxCoin": '1012',
"Pascal Lite": '1013',
"AmberCoin": '1014',
"Prototanium": '1015',
"Tattoocoin (Standard Edition)": '1016',
"KushCoin": '1017',
"Colossuscoin V2": '1018',
"MetalCoin": '1019',
"FIMKrypto": '1020',
"Mincoin": '1021',
"8Bit": '1022',
"Casino": '1023',
"Bankcoin": '1024',
"WayGuide": '1025',
"FinCoin": '1026',
"BTSR": '1027',
"Valorbit": '1028',
"SatoshiMadness": '1029',
"BTCtalkcoin": '1030',
"GlobalCoin": '1031',
"Bitz": '1032',
"Stress": '1033',
"Joincoin": '1034',
"PX": '1035',
"Rasputin Online Coin": '1036',
"Remicoin": '1037',
"Rubies": '1038',
"Grantcoin": '1039',
"Jin Coin": '1040',
"Bitcoin Planet": '1041',
"Dollarcoin": '1042',
"WMCoin": '1043',
"Mao Zedong": '1044',
"Shadow Token": '1045',
"SecretCoin": '1046',
"ETHGAS": '1047',
"SproutsExtreme": '1048',
"Virta Unique Coin": '1049',
"Freicoin": '1050',
"Sling": '1051',
"IslaCoin": '1052',
"Enigma": '1053',
"Global Tour Coin": '1054',
"Franko": '1055',
"Yacoin": '1056',
"Jewels": '1057',
"Firecoin": '1058',
"TajCoin": '1059',
"Crypto": '1060',
"Impact": '1061',
"eREAL": '1062',
"SACoin": '1063',
"Debitcoin": '1064',
"VectorAI": '1065',
"AntiBitcoin": '1066',
"Ripto Bux": '1067',
"HealthyWormCoin": '1068',
"Bitcoin 21": '1069',
"GuccioneCoin": '1070',
"Californium": '1071',
"Metal Music Coin": '1072',
"Asiadigicoin": '1073',
"Dreamcoin": '1074',
"Blackstar": '1075',
"GBCGoldCoin": '1076',
"ZetaMicron": '1077',
"BillaryCoin": '1078',
"BeaverCoin": '1079',
"iDice": '1080',
"Quebecoin": '1081',
"Ride My Car": '1082',
"MindCoin": '1083',
"Braincoin": '1084',
"FlavorCoin": '1085',
"CryptoWorldX Token": '1086',
"PIECoin": '1087',
"WARP": '1088',
"JavaScript Token": '1089',
"Uro": '1090',
"CryptoEscudo": '1091',
"PLNcoin": '1092',
"Zayedcoin": '1093',
"DAPPSTER": '1094',
"BiosCrypto": '1095',
"VIP Tokens": '1096',
"Litecred": '1097',
"GameBet Coin": '1098',
"ARbit": '1099',
"TAGRcoin": '1100',
"JobsCoin": '1101',
"Zonecoin": '1102',
"Destiny": '1103',
"Wild Beast Block": '1104',
"Unrealcoin": '1105',
"PonziCoin": '1106',
"PosEx": '1107',
"Pulse": '1108',
"RSGPcoin": '1109',
"OsmiumCoin": '1110',
"High Voltage": '1111',
"EGO": '1112',
"Orlycoin": '1113',
"LetItRide": '1114',
"Xonecoin": '1115',
"BowsCoin": '1116',
"ImpulseCoin": '1117',
"CRTCoin": '1118',
"Corethum": '1119',
"SydPak": '1120',
"iBank": '1121',
"Antilitecoin": '1122',
"Save and Gain": '1123',
"P7Coin": '1124',
"NodeCoin": '1125',
"GeyserCoin": '1126',
"CCMiner": '1127',
"Selfiecoin": '1128',
"Lex4All": '1129',
"CoffeeCoin": '1130',
"PizzaCoin": '1131',
"BurstOcean": '1132',
"ATMCoin": '1133',
"AI Doctor": '1134',
"SwftCoin": '1135',
"Odyssey": '1136',
"OFCOIN": '1137',
"SmartMesh": '1138',
"TopChain": '1139',
"All Sports": '1140',
"Show": '1141',
"Genaro Network": '1142',
"DATA": '1143',
"Zilliqa": '1144',
"Qbao": '1145',
"WaykiChain": '1146',
"Bitcoin Diamond": '1147',
"CoinMeet": '1148',
"LightChain": '1149',
"SingularityNET": '1150',
"Viuly": '1151',
"ChatCoin": '1152',
"LinkEye": '1153',
"Yee": '1154',
"Scry.info": '1155',
"CRYPTO20": '1156',
"Kcash": '1157',
"BitcoinX": '1158',
"Olympus Labs": '1159',
"EchoLink": '1160',
"SpaceChain": '1161',
"RefToken": '1162',
"True Chain": '1163',
"Fortuna": '1164',
"Aidos Kuneen": '1165',
"Bottos": '1166',
"indaHash": '1167',
"FairGame": '1168',
"OriginTrail": '1169',
"Super Bitcoin": '1170',
"Acute Angle Cloud": '1171',
"Energo": '1172',
"Hyper Pay": '1173',
"RealChain": '1174',
"carVertical": '1175',
"SelfSell": '1176',
"IPChain": '1177',
"COMSA [ETH]": '1178',
"Bitcoin Atom [Futures]": '1179',
"StarChain": '1180',
"Mobius": '1181',
"Lightning Bitcoin [Futures]": '1182',
"EDUCare": '1183',
"Molecular Future": '1184',
"COMSA [XEM]": '1185',
"UG Token": '1186',
"Ignis": '1187',
"Hydro Protocol": '1188',
"Profile Utility Token": '1189',
"SegWit2x": '1190',
"Hackspace Capital": '1191',
"ugChain": '1192',
"Read": '1193',
"AidCoin": '1194',
"United Bitcoin": '1195',
"Qube": '1196',
"Fargocoin": '1197',
"AICHAIN": '1198',
"Rebellious": '1199',
"HomeBlockCoin": '1200',
"POLY AI": '1201',
"Tezos (Pre-Launch)": '1202',
"StrongHands": '1203',
"Pundi X": '1204',
"InsurePal": '1205',
"EtherDelta Token": '1206',
"EA Coin": '1207',
"aXpire": '1208',
"Titanium Blockchain": '1209',
"InfChain": '1210',
"Crypterium": '1211',
"CFun": '1212',
"UnlimitedIP": '1213',
"TokenClub": '1214',
"InvestDigital": '1215',
"Maggie": '1216',
"Filecoin [Futures]": '1217',
"Measurable Data Token": '1218',
"Content and AD Network": '1219',
"MOAC": '1220',
"BitSoar": '1221',
"AWARE": '1222',
"Coinlancer": '1223',
"Infinitecoin": '1224',
"Gatcoin": '1225',
"Bitcoin Lightning": '1226',
"WETH": '1227',
"Royalties": '1228',
"BigONE Token": '1229',
"Swisscoin": '1230',
"Decentralized Universal Basic Income": '1231',
"Numus": '1232',
"Jiyo": '1233',
"TOKYO": '1234',
"BlockCDN": '1235',
"Smartlands": '1236',
"DavorCoin": '1237',
"CryptopiaFeeShares": '1238',
"PressOne": '1239',
"Matrix AI Network": '1240',
"Tokugawa": '1241',
"Vezt": '1242',
"MergeCoin": '1243',
"Tokenbox": '1244',
"Sphre AIR ": '1245',
"Bankex": '1246',
"Zap": '1247',
"Mixin": '1248',
"PlusCoin": '1249',
"Infinity Economics": '1250',
"ArbitrageCT": '1251',
"StrikeBitClub": '1252',
"Safe Trade Coin": '1253',
"Sparks": '1254',
"Elacoin": '1255',
"Ignition": '1256',
"ClubCoin": '1257',
"Cloud": '1258',
"Jingtum Tech": '1259',
"Harvest Masternode Coin": '1260',
"CasinoCoin": '1261',
"B3Coin": '1262',
"Galactrum": '1263',
"TimesCoin": '1264',
"Happy Creator Coin": '1265',
"Bitcoin God": '1266',
"FidentiaX": '1267',
"Golos Gold": '1268',
"Granite": '1269',
"GOLD Reward Token": '1270',
"Nitro": '1271',
"Maverick Chain": '1272',
"Bitair": '1273',
"BitSerial": '1274',
"NamoCoin": '1275',
"DIMCOIN": '1276',
"GameChain System": '1277',
"ATN": '1278',
"MSD": '1279',
"OX Fina": '1280',
"BOScoin": '1281',
"HTML5COIN": '1282',
"Chronologic": '1283',
"Garlicoin": '1284',
"IDEX Membership": '1285',
"LiteCoin Gold": '1286',
"Golfcoin": '1287',
"Cyder": '1288',
"MagicCoin": '1289',
"GUESS": '1290',
"TerraNova": '1291',
"Phantomx": '1292',
"VPNCoin": '1293',
"BT2 [CST]": '1294',
"Starbase": '1295',
"FireFlyCoin": '1296',
"SIGMAcoin": '1297',
"Matryx": '1298',
"Akuya Coin": '1299',
"ShareX": '1300',
"Animecoin": '1301',
"Protean": '1302',
"DeusCoin": '1303',
"Storjcoin X": '1304',
"EncryptoTel [ETH]": '1305',
"EDRCoin": '1306',
"United Traders Token": '1307',
"Alphabit": '1308',
"NEO GOLD": '1309',
"Kzcash": '1310',
"T-coin": '1311',
"Natcoin": '1312',
"Peacecoin": '1313',
"Cubits": '1314',
"Escroco": '1315',
"Fonziecoin": '1316',
"India Coin": '1317',
"TechShares": '1318',
"Francs": '1319',
"PlexCoin": '1320',
"Ethereum Lite": '1321',
"SHACoin": '1322',
"Triaconta": '1323',
"IrishCoin": '1324',
"WeAreSatoshi": '1325',
"SISA": '1326',
"Wowcoin": '1327',
"XDE II": '1328',
"PeepCoin": '1329',
"Zilbercoin": '1330',
"Compcoin": '1331',
"Soma": '1332',
"Macro": '1333',
"FlappyCoin": '1334',
"Facecoin": '1335',
"netBit": '1336',
"SafeCoin": '1337',
"Fazzcoin": '1338',
"MarxCoin": '1339',
"GlassCoin": '1340',
"HODL Bucks": '1341',
"Internet of Things": '1342',
"Sharkcoin": '1343',
"Bastonet": '1344',
"TodayCoin": '1345',
"Bitcedi": '1346',
"DynamicCoin": '1347',
"Everus": '1348',
"NumusCash": '1349',
"LandCoin": '1350',
"Bitok": '1351',
"Rcoin": '1352',
"ZenGold": '1353',
"Blockchain Index": '1354',
"Aces": '1355',
"Wink": '1356',
"GAY Money": '1357',
"TopCoin": '1358',
"BestChain": '1359',
"ZSEcoin": '1360',
"RubleBit": '1361',
"Sakuracoin": '1362',
"eGold": '1363',
"Pirate Blocks": '1364',
"Sand Coin": '1365',
"First Bitcoin": '1366',
"PinkDog": '1367',
"BetaCoin": '1368',
"Musiconomi": '1369',
"XTD Coin": '1370',
"iQuant": '1371',
"Bitbase": '1372',
"Antimatter": '1373',
"Donationcoin": '1374',
"UR": '1375',
"Bitcoin Silver": '1376',
"Tellurion": '1377',
"Vulcano": '1378',
"Pabyosi Coin (Special)": '1379',
"STEX": '1380',
"Wi Coin": '1381',
"Minex": '1382',
"eUSD": '1383',
"Rupaya [OLD]": '1384',
"Cycling Coin": '1385',
"High Gain": '1386',
"Nimfamoney": '1387',
"President Johnson": '1388',
"UniversalRoyalCoin": '1389',
"Magnetcoin": '1390',
"RabbitCoin": '1391',
"TurboCoin": '1392',
"Avoncoin": '1393',
"Moneta": '1394',
"Swapcoin": '1395',
"FAPcoin": '1396',
"AlpaCoin": '1397',
"BTCMoon": '1398',
"CORION": '1399',
"GoldMaxCoin": '1400',
"Halloween Coin": '1401',
"MoneyCoin": '1402',
"Regacoin": '1403',
"10M Token": '1404',
"UAHPay": '1405',
"Dutch Coin": '1406',
"Cheapcoin": '1407',
"Faceblock": '1408',
"EventChain": '1409',
"ANRYZE": '1410',
"Lazaruscoin": '1411',
"Primulon": '1412',
"Topaz Coin": '1413',
"President Trump": '1414',
"Digital Bullion Gold": '1415',
"iBTC": '1416',
"AvatarCoin": '1417',
"BitAlphaCoin": '1418',
"DarkLisk": '1419',
"Quotient": '1420',
"Cashme": '1421',
"PeopleCoin": '1422',
"TeraCoin": '1423',
"PayPeer": '1424',
"Dashs": '1425',
"Infinity Pay": '1426',
"RichCoin": '1427',
"X2": '1428',
"Xaucoin": '1429',
"eBIT": '1430',
"WA Space": '1431',
"PrismChain": '1432',
"Birds": '1433',
"Bitcoin2x": '1434',
"EggCoin": '1435',
"RHFCoin": '1436',
"Hyper": '1437',
"Huncoin": '1438',
"Axiom": '1439',
"LinkedCoin": '1440',
"TeamUp": '1441',
"Operand": '1442',
"Dubstep": '1443',
"Runners": '1444',
"Qora": '1445',
"The Vegan Initiative": '1446',
"Leek Coin": '1447',
"BlazerCoin": '1448',
"International Diamond": '1449',
"DeltaCredits": '1450',
"MobileCash": '1451',
"CBD Crystals": '1452',
"UGAIN": '1453',
"Tattoocoin (Limited Edition)": '1454',
"Opescoin": '1455',
"InvisibleCoin": '1456',
"Hyper TV": '1457',
"Karmacoin": '1458',
"Aseancoin": '1459',
"RoyalCoin": '1460',
"SportsCoin": '1461',
"Omicron": '1462',
"UNCoin": '1463',
"Bubble": '1464',
"SnakeEyes": '1465',
"ShellCoin": '1466',
"CyberCoin": '1467',
"PokeCoin": '1468',
"Yescoin": '1469',
"GameLeagueCoin": '1470',
"eLTC": '1471',
"MMXVI": '1472',
"First Bitcoin Capital": '1473',
"LePen": '1474',
"KashhCoin": '1475',
"FrankyWillCoin": '1476',
"FutCoin": '1477',
"Psilocybin": '1478',
"BITFID": '1479',
"Voyacoin": '1480',
"Cash Poker Pro": '1481',
"TrickyCoin": '1482',
"TheCreed": '1483',
"TeslaCoilCoin": '1484',
"LAthaan": '1485',
"UtaCoin": '1486',
"GoldUnionCoin": '1487',
"LLToken": '1488',
"WINCOIN": '1489',
"OCOW": '1490',
"Global Business Revolution": '1491',
"BT1 [CST]": '1492',
"ENTCash": '1493',
"KemCredit": '1494'
}

