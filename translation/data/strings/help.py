#!/usr/bin/python
# -*- coding: utf-8 -*-

# Special characters:
# _   Fast short tab (moves the cursor forward to the next 8 pixel column without any tile rendering involved)
# |   Short space
# <   1 pixel space
# [   Opening quotation mark
# ]   Closing quotation mark

# Control code characters:
# Manual kerning          ⏮n
# Extended character      ⏺nn
# Set VWF buffer offset   ⏫nn

# Space restrictions:
# 22 tiles max (176 pixels) for main text area lines (incl. one initial space, needed for nice layout).

strings = {

# HELP BAR
  0x918422: { "b":0x918422, "e":0x918436, "l":20, "en":"⏫00|Navegar____<Sair",    "ja":"せんたく　　　ぬける"  },

# SECTIONS (Upper left box)
  0x9184F3: { "b":0x9184F3, "e":0x918503, "l":16, "en":"⏫08_Seção A", "ja":"あそびかたの説明"  },
  0x918505: { "b":0x918505, "e":0x918515, "l":16, "en":"⏫10_Seção B", "ja":"マップコマンド　"  },
  0x918517: { "b":0x918517, "e":0x918527, "l":16, "en":"⏫08_Seção C", "ja":"部隊コマンド　　"  },

# PAGE NAVIGATION BAR

  # Guide A: General / Overview / How To Play
  0x9195C2: { "b":0x9195C2, "e":0x9195C8, "l":6,  "en":"_⏺81_",      "ja":"Ｐ１　"  },
  0x9195CA: { "b":0x9195CA, "e":0x9195D0, "l":6,  "en":"_⏺82_",      "ja":"Ｐ２　"  },
  0x9195D2: { "b":0x9195D2, "e":0x9195D8, "l":6,  "en":"_⏺83_",      "ja":"Ｐ３　"  },
  0x9195DA: { "b":0x9195DA, "e":0x9195E0, "l":6,  "en":"_⏺84_",      "ja":"Ｐ４　"  },
  0x9195E2: { "b":0x9195E2, "e":0x9195E8, "l":6,  "en":"_⏺85_",      "ja":"Ｐ５　"  },
  0x9195EA: { "b":0x9195EA, "e":0x9195F0, "l":6,  "en":"_⏺86_",      "ja":"Ｐ６　"  },
  0x9195F2: { "b":0x9195F2, "e":0x9195F8, "l":6,  "en":"_⏺87_",      "ja":"Ｐ７　"  },
  0x9195FA: { "b":0x9195FA, "e":0x919600, "l":6,  "en":"_⏺88_",      "ja":"Ｐ８　"  },
  0x919602: { "b":0x919602, "e":0x919608, "l":6,  "en":"_⏺89_",      "ja":"Ｐ９　"  },
  0x91960A: { "b":0x91960A, "e":0x919610, "l":6,  "en":"⏺81⏺80_",   "ja":"Ｐ１０"  },
  0x919612: { "b":0x919612, "e":0x919618, "l":6,  "en":"⏺81⏺81_",   "ja":"Ｐ１１"  },
  0x91961A: { "b":0x91961A, "e":0x919620, "l":6,  "en":"⏺81⏺82_",   "ja":"Ｐ１２"  },
  0x919622: { "b":0x919622, "e":0x919628, "l":6,  "en":"⏺81⏺83_",   "ja":"Ｐ１３"  },
  0x91962A: { "b":0x91962A, "e":0x919630, "l":6,  "en":"⏺81⏺84_",   "ja":"Ｐ１４"  },
  0x919632: { "b":0x919632, "e":0x919638, "l":6,  "en":"⏺81⏺85_",   "ja":"Ｐ１５"  },

  # Guide B: Main Commands
  0x91963A: { "b":0x91963A, "e":0x919640, "l":6,  "en":"_⏺81_",      "ja":"生産　"  }, # Deploying Units (1)
  0x919642: { "b":0x919642, "e":0x919648, "l":6,  "en":"_⏺82_",      "ja":"生産２"  }, # Deploying Units (2)
  0x91964A: { "b":0x91964A, "e":0x919650, "l":6,  "en":"_⏺83_",      "ja":"説明　"  }, # Help
  0x919652: { "b":0x919652, "e":0x919658, "l":6,  "en":"_⏺84_",      "ja":"部隊　"  }, # Units
  0x91965A: { "b":0x91965A, "e":0x919660, "l":6,  "en":"_⏺85_",      "ja":"全補　"  }, # Supply (1)
  0x919662: { "b":0x919662, "e":0x919668, "l":6,  "en":"_⏺86_",      "ja":"全補２"  }, # Supply (2)
  0x91966A: { "b":0x91966A, "e":0x919670, "l":6,  "en":"_⏺87_",      "ja":"全補３"  }, # Supply (3)
  0x919672: { "b":0x919672, "e":0x919678, "l":6,  "en":"_⏺88_",      "ja":"状況　"  }, # Intel
  0x91967A: { "b":0x91967A, "e":0x919680, "l":6,  "en":"_⏺89_",      "ja":"設定　"  }, # Options
  0x919682: { "b":0x919682, "e":0x919688, "l":6,  "en":"⏺81⏺80_",   "ja":"処分　"  }, # Dismiss
  0x91968A: { "b":0x91968A, "e":0x919690, "l":6,  "en":"⏺81⏺81_",   "ja":"降伏　"  }, # Retreat
  0x919692: { "b":0x919692, "e":0x919698, "l":6,  "en":"⏺81⏺82_",   "ja":"再戦　"  }, # Load
  0x91969A: { "b":0x91969A, "e":0x9196A0, "l":6,  "en":"⏺81⏺83_",   "ja":"休戦　"  }, # Save
  0x9196A2: { "b":0x9196A2, "e":0x9196A8, "l":6,  "en":"⏺81⏺84_",   "ja":"終了　"  }, # End Day
  0x9196AA: { "b":0x9196AA, "e":0x9196B0, "l":6,  "en":"___",          "ja":"　　　"  },

  # Guide C: Unit Commands
  0x9196B2: { "b":0x9196B2, "e":0x9196B8, "l":6,  "en":"_⏺81_",      "ja":"攻撃　"  }, # Attack (1)
  0x9196BA: { "b":0x9196BA, "e":0x9196C0, "l":6,  "en":"_⏺82_",      "ja":"攻撃２"  }, # Attack (2)
  0x9196C2: { "b":0x9196C2, "e":0x9196C8, "l":6,  "en":"_⏺83_",      "ja":"待機　"  }, # End Day
  0x9196CA: { "b":0x9196CA, "e":0x9196D0, "l":6,  "en":"_⏺84_",      "ja":"占領　"  }, # Capture (1)
  0x9196D2: { "b":0x9196D2, "e":0x9196D8, "l":6,  "en":"_⏺85_",      "ja":"占領２"  }, # Capture (2)
  0x9196DA: { "b":0x9196DA, "e":0x9196E0, "l":6,  "en":"_⏺86_",      "ja":"合流　"  }, # Join
  0x9196E2: { "b":0x9196E2, "e":0x9196E8, "l":6,  "en":"_⏺87_",      "ja":"補給　"  }, # Supply (1)
  0x9196EA: { "b":0x9196EA, "e":0x9196F0, "l":6,  "en":"_⏺88_",      "ja":"補給２"  }, # Supply (2)
  0x9196F2: { "b":0x9196F2, "e":0x9196F8, "l":6,  "en":"_⏺89_",      "ja":"搭載　"  }, # Load (1)
  0x9196FA: { "b":0x9196FA, "e":0x919700, "l":6,  "en":"⏺81⏺80_",   "ja":"搭載２"  }, # Load (2)
  0x919702: { "b":0x919702, "e":0x919708, "l":6,  "en":"⏺81⏺81_",   "ja":"搭載３"  }, # Load (3)
  0x91970A: { "b":0x91970A, "e":0x919710, "l":6,  "en":"⏺81⏺82_",   "ja":"降車　"  }, # Drop
  0x919712: { "b":0x919712, "e":0x919718, "l":6,  "en":"___",         "ja":"　　　"  },
  0x91971A: { "b":0x91971A, "e":0x919720, "l":6,  "en":"___",         "ja":"　　　"  },
  0x919722: { "b":0x919722, "e":0x919728, "l":6,  "en":"___",         "ja":"　　　"  },



# SECTION A: "How To Play"

  # A0: Table of Contents
  0x91979E: { "b":0x91979E, "e":0x9197BA, "l":28, "en":"⏫20 Manual de campo________", "ja":"　　　　ページの説明　　　　"  },
  0x919DFE: { "en":[
    " Bem-vindo ao treinamento! A Seção A",
    " é o seu Manual de Campo básico, que",
    " contém uma visão geral de como jogar..",
    "__   SUPER FAMICOM WARS!",
    " Descubra informações uteis para COs",
    " novatos e experientes. Atenção!",
    " Use cima/baixo {|} para virar",
    " páginas, e esquerda/direita para",
    " mudar de seção."
  ], "ja": [
    "　この「あそびかたの説明」は、下のようなペー",
    "ジでなりたっています。目をとおしてみてくださ",
    "い。",
    "　Ｐ１　〜Ｐ９　　　あそびかたの説明　　　　"
    "　Ｐ１０〜Ｐ１１　　さくてきモードの説明",
    "　Ｐ１２　　　　　　同盟の説明",
    "　Ｐ１３〜Ｐ１５　　わんぽいんとあどばいす",
    "",
    "　また　　の左右で説明をきりかえられます。"
  ]},

  # A1: Field Manual
  0x9197BC: { "b":0x9197BC, "e":0x9197D8, "l":28, "en":"⏫20 A1: Introdução_______", "ja":"　　　あそびかたの説明　　　"  },
  0x91BC8E: { "en":[
    " Começaremos com o treinamento básico.",
    "",
    " Isto cobrirá os objetivos da missão,",
    " como construir e mover suas forças",
    " ao redor e interagir com o inimigo.",
    " Concluiremos esta seção com atalhos",
    " de botões, modo de Neblina de Guerra,",
    " Relações Diplomáticas e alguns,",
    " conselhos adicionais."
  ], "ja": [
    "　あそびかたの説明は、",
    "Ｐ２　　　　　何をすればいいの？",
    "Ｐ３〜Ｐ４　　何を生産する？",
    "Ｐ５〜Ｐ６　　どう行動する？",
    "Ｐ７　　　　　占領しよう！　",
    "Ｐ８　　　　　さあ攻撃だ！　",
    "Ｐ９　　　　　おわりに　　　",
    "　となっています。基本をひととおりかいてます"
    "ので、はじめてのかたはよんでください。"
  ]},

  # A2: Mission Objective
  0x9197DA: { "b":0x9197DA, "e":0x9197F6, "l":28, "en":"⏫20 A2: Objetivo da missão____", "ja":"　　　何をすればいいの？　　"  },
  0x91BDC4: { "en":[
    " O objetivo do jogo é ou destruir",
    " todas as forças inimigas, ou capturar",
    " o QG{{} inimigo. Alcance estes",
    " objetivos criando um exército e",
    " enfrentando o inimigo pelo mapa.",
    " Da mesma forma, você será derrotado",
    " se todas as suas unidades forem",
    " destruídas ou se o seu QG{{} for",
    " capturado pelo inimigo."
  ], "ja": [
    "　ゲームの目的は、敵を全滅、もしくは敵の首都",
    "を占領することです。全滅させられたり、こちら",
    "の首都を占領されたりすると負けです。　",
    "　目的をたっせいするには、ユニットを生産し、",
    "占領ポイントを占領して収入をふやし、敵を攻撃",
    "して勝たねばなりません。　　　　　　　　　　"
  ]},

  # A3: Building An Army 1/2
  0x9197F8: { "b":0x9197F8, "e":0x919814, "l":28, "en":"⏫20 A3: Criar exército_|1⏮1|/|2_", "ja":"　　何を生産する？　その１　"  },
  0x91BF0E: { "en":[
    " Cada CO precisa de um exército. Para",
    " implantar sua primeira unidade, mova o",
    " cursor para seu QG{{}e pressione{|<}",
    " quando o cursor mudar para {{}. Seus",
    " fundos{}para construir são exibidos ao",
    " lado do ícone. Comece implantando uma",
    " unidade básica, como uma Infantaria {}",
    " ou Mecanizada{}."
  ], "ja": [
    "　はじめにすることは生産です。カーソル　　が",
    "　　　にかわるところで　　をおしてください。",
    "　自軍の色の首都　　と、そこにちかい工場　　",
    "空港　　港　　駅　　でかわるはずです。",
    "　生産するにはお金がいります。　　のとなりの",
    "数が今の自分のお金です。これより高いユニット",
    "はグレーで表示され、生産できません。　　　　",
    "　まず、歩兵　　か戦闘工兵　　を生産してくだ",
    "さい。"
  ]},

  # A4: Building An Army 2/2
  0x919816: { "b":0x919816, "e":0x919832, "l":28, "en":"⏫20 A4: Criar exército_2⏮1|/|2_", "ja":"　　何を生産する？　その２　"  },
  0x91C090: { "en":[
    " A Infantaria {} é barata, mas fraca.",
    " Mecanizadas{} são mais caras e menos",
    " móveis, porem fortes. Apenas esses",
    " dois tipos de unidades podem capturar",
    " edificações, então podem ser essenciais",
    " para a vitória. Aperte{|<}sobre uma",
    " unidade para ver suas estatísticas",
    " de combate. Ao terminar de construir,",
    " selecione [Finalizar] para continuar."
  ], "ja": [
    "　歩兵　　は安いがよわい、戦闘工兵　　は高く",
    "移動力も少ないがそこそこつよい、という個性が",
    "あります。占領できるのはこの２ユニットだけな",
    "ので、多めに生産しておいてください。",
    "　何が何につよい、どこを移動できるという個性",
    "は、ユニットごとにありますので、生産するとき",
    "に　　をおして、かくにんしてみてださい。　　",
    "　１日目は生産だけになります。終了をえらんで",
    "ください。"
  ]},

  # A5: Moving Out! 1/2
  0x919834: { "b":0x919834, "e":0x919850, "l":28, "en":"⏫20 A5: Movendo-se!_|1⏮1|/|2_", "ja":"　　どう行動する？　その１　"  },
  0x91C214: { "en":[
    " Pressionar{|<}em uma unidade",
    " destacará as áreas onde ela pode se",
    " mover. Ex: mova a Infantaria {} e",
    " a Mecanizada {} em direção as",
    " edificações antes de capturá-las.",
    " Então implante mais unidades fortes,",
    " como tanques, e mova-os para perto",
    " como proteção. Ou para atacar o",
    " inimigo."
  ], "ja": [
    "　さきほど生産したユニットの上で　　をおして",
    "ください。ユニットを中心にマップの色がかわり",
    "ます。色がかわったはんい内が、ユニットの移動",
    "はんいです。",
    "　歩兵　　や戦闘工兵　　なら、占領ポイントの",
    "上もしくはちかくに、戦車など攻撃がつよいユニ",
    "ットは歩兵　　や戦闘工兵　　を守るように動く",
    "か、敵ユニットと闘いに行くのがよいでしょう。"
  ]},

  # A6: Moving Out! 2/2
  0x919852: { "b":0x919852, "e":0x91986E, "l":28, "en":"⏫20 A6: Movendo-se!_2⏮1|/|2_", "ja":"　　どう行動する？　その２　"  },
  0x91C376: { "en":[
    " Ao enfrentar terreno difícil, ou para",
    " cobrir longas distancias rapidamente,",
    " use BTPs { }, Cargueiros {} e Heli",
    " Transporte { }. Por exemplo,",
    " embarque uma Infantaria {} em um Heli",
    " Transporte{}.<O embarque consumirá",
    " um turno. No dia seguinte, mova o",
    " Helicóptero { } sobre terra ou mar e",
    " desembarque o soldado em solo firme."
  ], "ja": [
    "　海などにはばまれて、そのユニットでは移動で",
    "きないとき、きょりがとおくて、移動するのに何",
    "日もかかるときには、輸送ヘリ　　や輸送船　　",
    "などに載っていくといいでしょう。",
    "　たとえば、空港　　で輸送ヘリ　　をつくり、",
    "歩兵　　を輸送ヘリ　　の上に移動させてみてく",
    "ださい。つぎの日から輸送ヘリ　　の移動力で動",
    "けるので、とおくまではこべます。"
  ]},

  # A7: Capturing Buildings
  0x919870: { "b":0x919870, "e":0x91988C, "l":28, "en":"⏫20 A7: Capturar edificação___", "ja":"　　　　占領しよう！　　　　"  },
  0x91C4E0: { "en":[
    " Ao mover sua Infantaria {} ou",
    " Mecanizada {}para uma edificação não",
    " controlada atualmente pelo seu exército,",
    " vice terá a opção de Capturá-la.",
    " As edificações tem 20 pontos de",
    " captura, então uma unidade de",
    " Infantaria {} ou Mecanizada {} com",
    " seus 10{}|completos pode capturá-la",
    " em dois dias consecutivos."
  ], "ja": [
    "　歩兵　　や戦闘工兵　　を自分の色以外の占領",
    "ポイントに移動させてください。「占領」という",
    "コマンドがでますので決定してください。　　　",
    "　占領ポイントにはたいきゅう力があります。ふ",
    "だんは２０あり、歩兵　　や戦闘工兵　　が　　",
    "１０のときに、２日で占領できます。　　　　　"
  ]},

  # A8: Engage The Enemy!
  0x91988E: { "b":0x91988E, "e":0x9198AA, "l":28, "en":"⏫20 A8: Enfrentar o inimigo!___", "ja":"　　　　さあ攻撃だ！　　　　"  },
  0x91C60A: { "en":[
    " Ao atacar, use unidades mais fortes e",
    " tire vantagem do terreno. Consulte as",
    " informações do terreno pressionando",
    " {|<}acima dele. A proximidade é crucial",
    " para a maioria das unidades ao atacar,",
    " enquanto a Artilharia {|} pode atacar",
    " indiretamente. Após se mover, as",
    " unidades de ataque indireto não podem",
    " atacar, portanto, mova-as com cautela."
  ], "ja": [
    "　敵がじゃまな所にいたり、こちらのじゃまをし",
    "てきたら戦闘をしましょう。戦闘をしかけるとき",
    "は、敵よりゆうりな地形で、つよいユニットでが",
    "基本です。それぞれ地形やユニットの上で　　を",
    "おして、かくにんしてください。",
    "　基本的にとなりにいる敵ユニットに行える「攻",
    "撃」ですが、　　　が２以上のユニットはかんせ",
    "つ攻撃できます。移動したあとすぐには攻撃でき",
    "ませんが、つよいのでうまくつかいましょう。"
  ]},

  # A9: Button Shortcuts
  0x9198AC: { "b":0x9198AC, "e":0x9198C8, "l":28, "en":"⏫20 A9: Botões de atalho____", "ja":"　　　　　おわりに　　　　　"  },
  0x91C7A8: { "en":[
    " Existem atalhos para COs eficientes:",
    "____Exibe{} para todas as unidades",
    "____e se estão carregadas.",
    "____Move rapidamente o cursor",
    "____entre o QG {} de cada exército.",
    "____Move rapidamente o cursor",
    "____entre unidades ainda não movidas.",
    "",  # Leave blank (row of icons)
    "____Reinicia o jogo."
  ], "ja": [
    "　さいごに、べんりなキーの説明をします。",
    "　　　　がめん中の全ユニットの　　と、搭載状",
    "　　　　況をみることができます。",
    "　　　　赤軍、青軍、　軍、　軍のじゅんばんで",
    "　　　　首都　　にカーソル　　がいきます。",
    "　　　　まだ行動していないユニットにカーソル",
    "　　　　　　がいきます。",
    "",
    "　　　　リセットできます。"
  ]},

  # A10: Fog of War 1/2
  0x9198CA: { "b":0x9198CA, "e":0x9198E6, "l":28, "en":"⏫20 A10: Neb. de guerra  <1⏮1|/|2_", "ja":"　　さくてきモード　その１　"  },
  0x91C8F2: { "en":[
    " Na Neblina de Guerra,|sua visão do mapa",
    " é limitada, sendo visíveis apenas as",
    " edificações do seu exército e aliados,",
    " além de áreas ao alcance { | } de suas",
    " unidades.<Movimentos inimigos fora desse",
    " alcance são indetectáveis. Infantaria {}",
    " e Mecanizada {} ganham uma util",
    " habilidade ao subir montanhas __<|,",
    " aumentando sua visão em 3."
  ], "ja": [
    "　索敵はんい外はみえなくなるモードです。",
    "　索敵はんいは、自軍と同盟軍の占領ポイントの",
    "上、自軍と同盟軍ユニットの　　　内となってい",
    "ます。　　　　　　　　　　　　　　　　　　",
    "　歩兵　　と戦闘工兵　　は山　　の上にいると",
    "索敵はんいにプラス３されます。　　　　　　　"
  ]},

  # A11: Fog of War 2/2
  0x9198E8: { "b":0x9198E8, "e":0x919904, "l":28, "en":"⏫20 A11: Neb. de guerra_2⏮1|/|2_", "ja":"　　さくてきモード　その２　"  },
  0x91CA18: { "en":[
    " Se uma unidade se mover para o",
    " caminho de um inimigo oculto na",
    " Neblina de Guerra, o turno da unidade",
    " será encerrado.|Neste modo,|Submarinos",
    " {{<} não podem ser detectados, mesmo",
    " dentro do alcance de visão, a menos",
    " que estejam diretamente adjacentes",
    " a uma de suas unidades ou ancorados",
    " dentro de um porto{} ."
  ], "ja": [
    "　索敵はんい外、つまりマップがグレーになって",
    "いる場所に行動したとき、もしその目的地、もし",
    "くは移動とちゅうに敵がいたら「そうぐう」とな",
    "りきょうせい的に行動が終了させられます。",
    "　なお、潜水艦　　は索敵はんい内にいても、と",
    "なりあう、もしくはこちらの港　　にいないかぎ",
    "りみえません。"
  ]},

  # A12: Diplomatic Relations
  0x919906: { "b":0x919906, "e":0x919922, "l":28, "en":"⏫20 A12: Rel. diplomáticas   ___", "ja":"　　　　　　同盟　　　　　　"  },
  0x91CB4C: { "en":[
    " Em jogos de 4 jogadores, até dois COs",
    " podem se aliar para destruir unidades",
    " inimigas ou capturar o QG {}. Contudo,",
    " edificações aliadas são imunes à captura",
    " e não oferecem reparos ou fornecimento",
    " de unidades. Em resumo, é uma guerra,",
    " não um chá da tarde!"
  ], "ja": [
    "　同盟をむすぶことができるモードです。　　　",
    "　同盟したあいてとともに同盟軍と自軍以外の敵",
    "を全滅、もしくは首都占領してください。ただ、",
    "同盟軍の都市は占領することはできませんし、そ",
    "の都市の上で補充、補給することもできません。"
  ]},

  # A13: Advice 1/3
  0x919924: { "b":0x919924, "e":0x919940, "l":28, "en":"⏫20 A13: Dicas_____|1⏮1|/|3_", "ja":"　わんぽいんとあどばいす１　"  },
  0x91CC64: { "en":[
    " Capturando <-< Chamada por Reforços!",
    "",
	" Unidades podem ser atacadas enquanto",
    " capturam uma edificação. Se a unidade",
    " for eliminada, todo o progresso de",
    " captura será perdido. Isso pode ser",
    " evitado unindo outra unidade a ferida.",
    " A captura pode então continuar até a",
    " edificação ser tomada."
  ], "ja": [
    "　　　　　占領中に合流できること　　　　　",
    "",
    "・占領とちゅうに敵に攻撃されて、全滅したこ",
    "　とがあるとおもいます。そうしたらまたさい",
    "　しょからやりなおしになり、たいへんです。",
    "　そういうときには、占領しているユニットに",
    "　合流しましょう。占領ポイントからでたわけ",
    "　ではありませんから、そのままつづけて占領",
    "　できます。"
  ]},

  # A14: Advice 2/3
  0x919942: { "b":0x919942, "e":0x91995E, "l":28, "en":"⏫20 A14: Dicas_____2⏮1|/|3_", "ja":"　わんぽいんとあどばいす２　"  },
  0x91CDB8: { "en":[
    " Lembrando sua Patente:",
    "",
    " Ativar [Subir de nível] permite que as",
    " unidades aumentem de nível após um",
    " confronto.",
    " Note que se a unidade sofrer dano e se",
    " combinar a outra para aumentar o  },",
    " o maior dos níveis das duas unidades",
    " será mantido."
  ], "ja": [
    "　　　　　　　レベルと合流",
    "",
    "・さいしょの設定で、レベルアップを○●にす",
    "　ると戦闘でレベルが上がるようになりますが、",
    "　レベルが上がるころにはこちらのＨＰ　　も",
    "　少なくなっていることでしょう。そういうと",
    "　きにはレベルのひくいユニットを合流させて",
    "　みてください。レベルは高いほうがひきつが",
    "　れます。"
  ]},

  # A15: Advice 3/3
  0x919960: { "b":0x919960, "e":0x91997C, "l":28, "en":"⏫20 A15: Dicas_____3⏮1|/|3_", "ja":"　わんぽいんとあどばいす３　"  },
  0x91CEFC: { "en":[
    " Exponha e destrua:",
    "",
    " Durante a Neblina de Guerra, unidades",
    " indiretas não podem atacar áreas",
    " ocultas - mesmo sabendo que há um",
    " inimigo. Unidades com alcance",
    " amplo, como Reconhecimento {} e",
    " Cruzadores{} , podem ser enviadas",
    " primeiro para expor um alvo ao ataque."
  ], "ja": [
    "　　　　　　偵察車　　と護衛艦",
    "",
    "・索敵モードのときの索敵はんい外には、たと",
    "　えそこに敵がいるとしっていても、かんせつ",
    "　攻撃などをしかけることはできません。そう",
    "　いうときには　　　のひろい偵察車　　や護",
    "　衛艦　　などをすてるつもりで行かせましょ",
    "　う。少なくともその日は攻撃できるようにな",
    "　ります。"
  ]},



# SECTION B: "Main Commands"

  # B0
  0x91997E: { "b":0x91997E, "e":0x91999A, "l":28, "en":"⏫20 Comandos     ________", "ja":"　マップコマンドの説明　　　"  },
  0x919D3A: { "en":[
    " Na Seção B, vamos explorar os",
    " comandos disponíveis nos menus de alto",
    " nível e sistema. (Menus são uteis para",
    " mais do que suas rações na cantina.)",
    " Descubra informações uteis para COs",
    " novatos e experientes. Atenção!",
    " Use cima/baixo {|} para virar",
    " páginas, e esquerda/direita para",
    " mudar de seção."
  ], "ja": [
    "ぜんたいをかんりするためのコマンドです。　　",
    "　　　　　　　　　　　　　　　　　　　　　　"
  ]},

  # B1: Deploy 1/3
  0x91999C: { "b":0x91999C, "e":0x9199B8, "l":28, "en":"⏫20 B1: Produção_____|1⏮1|/|3_", "ja":"　　生産コマンドの説明その１"  },
  0x919F42: { "en":[
    " Se possuídas desde o início de uma",
    " batalha, pressione{|<}sobre essas",
    " edificações para produzir os seguintes",
    " tipos de unidades:",
    "___QG______ Unidades terrestres",
    "___Bases____ Unidades terrestres",
    "___Aeroportos_<<<Unidades aéreas",
    "___Portos____ Unidades navais",
    "___Depósitos__<<<Trens"
  ], "ja": [
    "　ユニットの生産を行うコマンドです。　　　　",
    "　生産ができる場所とは、　　　が　　　のよう",
    "に表示される場所、つまり自軍の首都　　をふく",
    "め２マス周辺の工場　　空港　　港　　駅　　で",
    "す。",
    "　生産は６０部隊までです。なお、列車砲　　を",
    "生産すると、こわされるまでは、あらたな列車砲",
    "を生産することはできません。"
  ]},

  # B2: Deploy 2/3
  0x9199BA: { "b":0x9199BA, "e":0x9199D6, "l":28, "en":"⏫20 B2: Produção____2⏮1|/|3_", "ja":"　　生産コマンドの説明その２"  },
  0x91A08C: { "en":[
    " Todo bom CO, em algum momento, se",
    " imaginou com um numero ilimitado de",
    " tropas a sua disposição.",
    "",
    " A realidade da guerra, no entanto,",
    " limita você a um máximo de 60 unidades",
    " sob seu comando de cada vez.|Isso inclui",
    " no máximo um trem por vez por CO. Não",
    " tente ultrapassar seus limites."
  ], "ja": [
    "　どこで何が生産できるか説明します。　　　　",
    "　　　　　　　・・・地上ユニット　　　　　　",
    "　　　　　　　・・・航空ユニット　　　　　　",
    "　　　　　　　・・・海上ユニット　　　　　　",
    "　　　　　　　・・・列車砲　　　　　　　　　"
  ]},

  # B3: Deploy 3/3
  0x9199D8: { "b":0x9199D8, "e":0x9199F4, "l":28, "en":"⏫20 B3: Produção____3⏮1|/|3_", "ja":"　　説明コマンドの説明　　　"  },
  0x91A182: { "en":[
    " COs bem-sucedidos capturam Bases",
    " inimigas, Aeroportos{|},|Portos{|} e",
    " Depósitos{|}. Edificações capturadas",
    " não produzem unidades,|mas oferecem",
    " reparos e suprimentos às unidades",
    " correspondentes devido à falta de",
    " pessoal. Para mais informações",
    " sobre isso, consulte B5."
  ], "ja": [
    "　このがめんをみることができるコマンドです。",
    "　各コマンドのかいせつやあそびかたを説明して",
    "いるので、こまったらみてください。　　　　　",
    "　　　　　　　　　　　　　　　　　　　　　　　"
  ]},

  # B4: Units
  0x9199F6: { "b":0x9199F6, "e":0x919A12, "l":28, "en":"⏫20 B4: Unidades________", "ja":"　　部隊コマンドの説明　　　"  },
  0x91A242: { "en":[
    " Na opção Unidades, veja todas as",
    " forças no campo de batalha. Use",
    " para ordenar por Tipo, Nível, PV{  ,",
    " Combustível|{} ou Munição{}.",
    " Navegue pela lista com cima ou baixo",
    " e pressione{|<}sobre uma unidade",
    " para localizá-la no mapa."
  ], "ja": [
    "　部隊いちらんを表示するコマンドです。　　　",
    "　　の左右でへいしゅ、レベル、ＨＰ　　、ねん",
    "りょう　　、弾　　のそれぞれについてならべか",
    "えることができます。",
    "　また、　　の上下で目的のユニットをえらび決",
    "定すると、マップ中のユニットへカーソル　　を",
    "移動させることができます。"
  ]},

  # B5: Supply 1/3
  0x919A14: { "b":0x919A14, "e":0x919A30, "l":28, "en":"⏫20 B5: Abastecer___|1⏮1|/|3_", "ja":"　　全補コマンドの説明その１"  },
  0x91A36E: { "en":[
    " Com o Autoabastecer ativado, unidades",
    " em edificações sob seu controle no",
    " início de um novo dia ganharão 2{|}e",
    " terão seu<{}<e<{}reabastecidos nestes",
    " locais:",
    "__________Unidades terrestres",
    "__________Unidades aéreas",
    "__________Unidades navais",
    "__________Trens"
  ], "ja": [
    "　全ユニットに補給、補充を行うコマンドです。",
    "　それぞれのユニットにたいおうした自軍占領ポ",
    "イントで、１日につき２だいの補充、　　　　の",
    "補給が行われます。どこで何が補充、補給をうけ",
    "られるかは下をみてください。　　　　　　　　",
    "　　　　　　　　　・・・地上ユニット　　　　",
    "　　　　　　　　　・・・航空ユニット　　　　",
    "　　　　　　　　　・・・海上ユニット　　　　",
    "　　　　　　　　　・・・列車砲　　　　　　　　"
  ]},

  # B6: Supply 2/3
  0x919A32: { "b":0x919A32, "e":0x919A4E, "l":28, "en":"⏫20 B6: Abastecer___2⏮1|/|3_", "ja":"　　全補コマンドの説明その２"  },
  0x91A51E: { "en":[
    " Claro, o pessoal do financeiro no QG",
    " (resmunga baixinho...) não nos permitem",
    " abastecer e reparar nossas forças de",
    " graça, Os custos em{|<}estão abaixo:",
    "",
    "__1/<10 do preço da unid. para reparar",
    "__1{|<<<por ponto de combust. abastecido",
    "__Depende do tipo de arma.  Aperte",
    "__enquanto sobre uma unidade para ver."
  ], "ja": [
    "　なお、つぎのじょうけんのユニットは　　　　",
    "の補給はされますが、補充はされません。　　　",
    "",
    "　補給車にりんせつした地上ユニットと　　　　",
    "　護衛艦に搭載された　　　　　　　　　　　　",
    "",
    "　全補は、すでに待機じょうたいになった（その",
    "日の行動がおわった）ユニットにたいしては、行",
    "われません。"
  ]},

  # B7: Supply 3/3
  0x919A50: { "b":0x919A50, "e":0x919A6C, "l":28, "en":"⏫20 B7: Abastecer___3⏮1|/|3_", "ja":"　　全補コマンドの説明その３"  },
  0x91A654: { "en":[
    " Reparos ocorrem em edificações, mas",
    " algumas unidades podem ser abastecidas",
    " com{<}<<<e{<} no campo, como Unidades",
    " Terrestres e {{}{}|próximas a um",
    " Caminhão de Suprimento e",
    " embarcadas em um Cruzador{|}. Se o",
    " Autoabastecer estiver desativado, use",
    " Suprir no menu para reabastecer",
    " unidades não movidas."
  ], "ja": [
    "　補充、補給にはお金がかかります。",
    "　補充には１だいにつきそのユニットの１／１０",
    "のねだんのお金がひつようです。",
    "　ねんりょう　　の補給は、１　ユニットの数",
    "つかったねんりょう、でもとめられます。",
    "　弾　　の補給は、ユニットごとにきめられた弾",
    "のねだんに、ユニットの数とつかった弾の数をか",
    "けたものです。弾のねだんはそれぞれのユニット",
    "の上で　　をおして、かくにんしてください。"
  ]},

  # B8: Intel
  0x919A6E: { "b":0x919A6E, "e":0x919A8A, "l":28, "en":"⏫20 B8: Intel.___________", "ja":"　　状況コマンドの説明　　　"  },
  0x91A7E0: { "en":[
    " A Inteligencia oferece dados sobre a",
    " batalha atual. A primeira página exibe",
    " as edificações, fundos, renda e",
    " unidades para cada exército.",
    "____Fundos disponíveis",
    "____Renda diária",
    " A segunda mostra informações de",
    " implantação. Use{|} para mudar o",
    " exército exibido."
  ], "ja": [
    "　ぜんたいの状況をはあくするコマンドです。　",
    "　それぞれの軍の占領状況や今もっているお金、",
    "収入や全ユニット数をみることができます。　",
    "　生産部隊数と全滅部隊数もここでみることがで",
    "きます。",
    "　　　　・・・今もっているお金",
    "　　　　・・・収入",
    "　です。"
  ]},

  # B9: Options
  0x919A8C: { "b":0x919A8C, "e":0x919AA8, "l":28, "en":"⏫20 B9: Opções________", "ja":"　　設定コマンドの説明　　　"  },
  0x91A8F0: { "en":[
    " Durante uma batalha, ainda é",
    " possível ajustar as seguintes opções:",
    "",
    " Autoabastecer_____<||⏺C0/⏺C1",
    " Batalha rápida<</|Mapa_||⏺C0/⏺C1",
    " Som___________ Mono</|Estéreo",
    "",
    " No modo 4J, é possível visualizar",
    " as Relações Diplomáticas entre COs."
  ], "ja": [
    "　ゲームの設定をみるコマンドです。",
    "　以下の設定をへんこうできます。",
    "　プレイヤーのオート全補　ＯＮ／ＯＦＦ　　　",
    "　かんい戦闘モード　　　　ＯＮ／ＯＦＦ　　　",
    "　こうそくモード　　　　　ＯＮ／ＯＦＦ　　　",
    "　サウンドの設定　　　　　　",
    "　また、４Ｐモードでは　　　　　もみることが",
    "できます。"
  ]},

  # B10: Disband
  0x919AAA: { "b":0x919AAA, "e":0x919AC6, "l":28, "en":"⏫20 B10: Dispensar_______", "ja":"　　処分コマンドの説明　　　"  },
  0x91AA2A: { "en":[
    " Pode haver momentos em que, por",
    " razões estratégicas, seja necessário",
    " remover uma unidade do campo de",
    " batalha.",
    " O comando Dispensar mudará",
    " o< cursor< de{{<}  para< este{{|} ,",
    " permitindo que você remova",
    " permanentemente a unidade selecionada",
    " pressionando{|<}acima dela."
    ""
  ], "ja": [
    "　自軍のユニットを処分できるコマンドです。　",
    "　処分コマンドをえらぶと、カーソルの形が、",
    "",
    "　　　から、　　　にかわるので、処分したいユ",
    "ニットへあわせ決定してください。　"
  ]},

  # B11: Retreat
  0x919AC8: { "b":0x919AC8, "e":0x919AE4, "l":28, "en":"⏫20 B11: Render-se_______", "ja":"　　降伏コマンドの説明　　　"  },
  0x91AAE0: { "en":[
    " P<) Qual é o resultado melhor:| Perder",
    " uma batalha ou se render primeiro<?",
    " R) V<E<N<C<E<R.",
    "",
    " No entanto, se você TIVER que deixar",
    " o campo de batalha atual, selecionar",
    " Render-se irá dispensar todas as suas",
    " unidades e permitir que todos os COs",
    " restantes lutem pela vitória."
  ], "ja": [
    "　戦いに降伏するコマンドです。　　　　　　　",
    "　降伏すると負けになってしまうので注意してく",
    "ださい。　　　　　　　　　　　　　　　　　　　"
  ]},

  # B12: Load
  0x919AE6: { "b":0x919AE6, "e":0x919B02, "l":28, "en":"⏫20 B12: Carregar________", "ja":"　　再戦コマンドの説明　　　"  },
  0x91AB70: { "en":[
    " Carregar irá carregar rapidamente do",
    " seu ponto de salvamento mais recente",
    " dentro do atual jogo. Isso, é claro,",
    " perderá qualquer progresso além do",
    " momento em que o salvamento foi feito.",
    "",
    " (<Se você começou um novo jogo, mas",
    " ainda não fez nenhum salvamento, esta",
    " opção ainda não estará disponível.<)"
  ], "ja": [
    "　休戦データを再開するコマンドです。　　　　",
    "　セーブしたところからやりなおしたいときにえ",
    "らんでください。　　　　　　　　　　　　　　　"
  ]},

  # B13: Save
  0x919B04: { "b":0x919B04, "e":0x919B20, "l":28, "en":"⏫20 B13: Salvar________", "ja":"　　休戦コマンドの説明　　　"  },
  0x91AC00: { "en":[
    " Mesmo o CO mais dedicado precisa",
    " deixar temporariamente o campo de",
    " batalha para rever suas estratégias",
    " ou talvez preparar um sanduíche.",
    " Escolher Salvar no menu salvará o",
    " estado atual da batalha para que você",
    " possa retornar mais tarde. Observe",
    " que isso sobrescreverá o estado",
    " de salvamento anterior."
  ], "ja": [
    "　今のじょうたいをほぞんするコマンドです。",
    "　休戦すると、まえのデータがきえてしまうので",
    "注意してください。　　　　　　　　　　　　　　"
  ]},

  # B14: End Day
  0x919B22: { "b":0x919B22, "e":0x919B3E, "l":28, "en":"⏫20 B14: Finalizar_______", "ja":"　　終了コマンドの説明　　　"  },
  0x91AC50: { "en":[
    " Se você terminou de implantar, mover,",
    " capturar, embarcar, desembarcar e",
    " atacar, selecione a opção [Finalizar]",
    " no menu.",
    " Isso permitirá que todos os outros COs",
    " comandem seus exércitos. Você",
    " retomará o comando do seu próprio",
    " quando todos os outros COs terminarem",
    " e um novo dia começar."
  ], "ja": [
    "　その日の行動を終了するコマンドです。　　　",
    "　　　　　　"
  ]},



# SECTION C: "Unit Commands"

  # C0
  0x919B40: { "b":0x919B40, "e":0x919B5C, "l":28, "en":"⏫20 Ordens_______________", "ja":"　　部隊コマンドの説明　　　"  },
  0x919DA0: { "en":[
    " Finalmente, a Seção C abordará talvez",
    " os comandos mais importantes: aqueles",
    " que permitem dar ordens diretas as",
    " suas unidades.",
    " Descubra informações uteis para COs",
    " novatos e experientes. Atenção!",
    " Use cima/baixo {|} para virar",
    " páginas, e esquerda/direita para",
    " mudar de seção."
  ], "ja": [
    "ユニットごとにしれいをあたえるコマンドです。",
    "　　　　　　　　　　　　　　　　　　　　　　"
  ]},

  # C1: Attack 1/2
  0x919B5E: { "b":0x919B5E, "e":0x919B7A, "l":28, "en":"⏫20 C1: Ataque_______|1⏮1|/|2_", "ja":"　　攻撃コマンドの説明その１"  },
  0x91ACCC: { "en":[
    " Alguns COs expressaram que ⏮1[Ataque]",
    " é sua palavra favorita. Ataques podem",
    " ser Diretos ou Indiretos. Armas de",
    " unidades com {{} de 1 causam dano",
    " próximo a uma unidade inimiga,",
    " enquanto {{} de 2 ou mais indicam",
    " ataques Indiretos à distância.",
    " Pressione{|<} em uma unidade para",
    " ver o seu{{}|."
  ], "ja": [
    "　敵に攻撃をしかけるコマンドです。　　　　　",
    "　攻撃はおおきくわけて、ちょくせつ攻撃とかん",
    "せつ攻撃の２つがあります。",
    "　　ちょくせつ攻撃は、　　　が１のユニットが",
    "敵ユニットととなりあったときにできます。攻撃",
    "コマンドをえらぶと、攻撃カーソル　　　がでる",
    "ので、敵をえらんでください。"
  ]},

  # C2: Attack 2/2
  0x919B7C: { "b":0x919B7C, "e":0x919B98, "l":28, "en":"⏫20 C2: Ataque_______2⏮1|/|2_", "ja":"　　攻撃コマンドの説明その２"  },
  0x91AE00: { "en":[
    " Armas Indiretas podem causar dano",
    " pesado, mas tem outra vantagem:",
    " Ataques Indiretos não permitem ao",
    " inimigo contra-atacar naquele turno.",
    " No entanto, lembre-se de que uma",
    " unidade não pode se mover e disparar",
    " uma arma Indireta no mesmo dia. Além",
    " disso, armas Indiretas tem um",
    " alcance mínimo de disparo."
  ], "ja": [
    "　かんせつ攻撃は　　　が２以上のユニットが行",
    "うことができます。さらに、はんげきをうけない",
    "ので、いっぽうてきにダメージをあたえることが",
    "できます。ただし、移動と攻撃を１日で行うこと",
    "はできません。",
    "　ちょくせつ攻撃ユニット、かんせつ攻撃ユニッ",
    "トともに攻撃できる敵がきまっているので、くわ",
    "しくしりたいかたはユニットの上で　　をおして",
    "かくにんしてください。"
  ]},

  # C3: Capture 1/2
  0x919B9A: { "b":0x919B9A, "e":0x919BB6, "l":28, "en":"⏫20 C3: Captura______|1⏮1|/|2_", "ja":"　　待機コマンドの説明　　　"  },
  0x91AF7A: { "en":[
    " Você prestou atenção, CO? Se sim,",
    " você já entendeu a importância da",
    " captura. Se não, revise as seções",
    " A7, A13 e B5!",
    " Aqueles que estudaram serão",
    " devidamente recompensados: Todas",
    " as edificações capturadas, exceto",
    " o QG {}, geram uma renda",
    " de 1|000{|} por dia."
  ], "ja": [
    "　ユニットの行動を終わらせるコマンドです。　",
    "　　　　　　　　　　　　　　　　　　　　　　"
  ]},

  # C4: Capture 2/2
  0x919BB8: { "b":0x919BB8, "e":0x919BD4, "l":28, "en":"⏫20 C4: Captura______2⏮1|/|2_", "ja":"　　占領コマンドの説明その１"  },
  0x91AFD8: { "en":[
    " A ciência trouxe descobertas",
    " incríveis, mas a pesquisa militar",
    " permite explosões ainda maiores.",
    " Capture um laboratório{<  } para",
    " desbloquear o poderoso Prototanque",
    " { }, e gerar 1|000{|} por dia. O",
    " é extremamente poderoso, sendo",
    " aconselhável capturar esses",
    " laboratórios sempre que possível."
  ], "ja": [
    "　占領ポイントを占領するコマンドです。　　　",
    "　自軍の色以外の首都　　工場　　都市　　研究",
    "所　　空港　　港　　駅　　に、歩兵　　か戦闘",
    "工兵　　を移動させると行えます。",
    "　これらの占領ポイントはたいきゅう力が２０あ",
    "り、　　１０のユニットが２日で占領できます。",
    "占領しかけのユニットがとちゅうでどこかへ移動",
    "したり、敵に全滅させられると、たいきゅう力が",
    "もどってしまうので注意してください。"
  ]},

  # C5: Join
  0x919BD6: { "b":0x919BD6, "e":0x919BF2, "l":28, "en":"⏫20 C5: Join____________", "ja":"　　占領コマンドの説明その２"  },
  0x91B172: { "en":[
    " Ultima explicação sobre o comando",
    " Combinar:",
    " Duas unidades do mesmo tipo podem se",
    " combinar ao ocuparem a mesma casa, a",
    " menos que ambas já tenham 10{}. A",
    " unidade resultante assume o maior",
    " e {|} e combina seus{||} até um total",
    " de 10. Unidades em transportes não",
    " podem ser combinadas."
  ], "ja": [
    "　首都　　以外は、占領すると収入　　が、つぎ",
    "の日から１０００ふえます。　　　　　　　　",
    "　研究所　　を中立のとき占領すると、新型戦車",
    "　　がてにはいります。研究所　　のそのあとの",
    "やくわりは都市　　とかわりませんが、新型戦車",
    "　　はおおきな戦力となりますのでがんばって占",
    "領してください。",
    "　れいがいとして、４Ｐマップのときの同盟して",
    "いる軍の占領ポイントは、占領できません。　"
  ]},

  # C6: Supply 1/2
  0x919BF4: { "b":0x919BF4, "e":0x919C10, "l":28, "en":"⏫20 C6: Supply_______|1⏮1|/|2_", "ja":"　　合流コマンドの説明　　　"  },
  0x91B300: { "en":[
    " O comando<[Abastecer]<é exclusivo dos",
    " Caminhões de Suprimento {}. Isso irá",
    " reabastecer unidades terrestres e",
    " helicópteros {}{}< com {}|e<{}.",
    " Todas as quatro unidades ao redor",
    " seriam abastecidas no exemplo mostrado",
    " a seguir:",
    # Note: The last 3 lines are dedicated to a figure showing a cross formation with Supply Truck in the center
  ], "ja": [
    "　おなじしゅるいのユニットを合流させるコマン",
    "ドです。　　　　　　　　　　　　　　　　　　",
    "　同じユニットの上に移動することで合流できま",
    "すが、りょうほう　　１０のときはできません。",
    "　合流すると、　　　　は多いほうがひきつがれ",
    "ます。　　は、たした数になりますが、１０をこ",
    "えるときりすてられます。　　　　　　　　　　",
    "　何かを搭載中のユニットは合流できませんので",
    "注意してください。　　　　　　　　　　　　　　"
  ]},

  # C7: Supply 2/2
  0x919C12: { "b":0x919C12, "e":0x919C2E, "l":28, "en":"⏫20 C7: Supply_______2⏮1|/|2_", "ja":"　　補給コマンドの説明その１"  },
  0x91B4B0: { "en":[
    " Suas unidades irão consumir {} durante",
    " o movimento pelo campo de batalha.",
    " No entanto, unidades Aéreas e Navais",
    " consomem {|}por dia, mesmo que não se",
    " movam. Se essas unidades ficarem sem",
    " {}, a unidade será perdida. Pressione",
    " {||} sobre uma unidade para revisar seu",
    " consumo diário de {} (e reveja seu",
    " treinamento sobre como reabastecer)."
  ], "ja": [
    "　補給車が補給を行うコマンドです。　　　　　",
    "　補給車　　ととなりあうマスにいるすべての地",
    "上ユニットと戦闘ヘリ　　、輸送ヘリ　　に、ね",
    "んりょう　　と弾　　の補給ができます。　　　",
    "　ただし、補充はできません。"
  ]},

  # C8: Load 1/3
  0x919C30: { "b":0x919C30, "e":0x919C4C, "l":28, "en":"⏫20 C8: Load________|1⏮1|/|3_", "ja":"　　補給コマンドの説明その２"  },
  0x91B59E: { "en":[
    " Cada tipo de transporte tem uma",
    " capacidade de embarque diferente.",
    " Estude o que cada um pode embarcar",
    " abaixo:",
    "__ |BTP_____    ⏮1|1_*___| ou",
    "__ |Heli Transporte__⏮1|1_*___| ou",
    "__ |Cargueiro___2_*_ Unid. terrestres",
    "__ |Cruzador___2_*___| ou",
    "__ |Trem_____2_*_ Unid. terrestres"
  ], "ja": [
    "　補給にはお金がかかります。くわしいことは、",
    "「全補３」のページをみてください。",
    "",
    "　航空ユニットと海上ユニットは、１日ごとに、",
    "たとえ場所を移動しなくとも、ねんりょう　　が",
    "へっていきます。ねんりょう　　が０になると、",
    "ついらく（ちんぼつ）してしまうので注意してく",
    "ださい。ユニットの上で　　をおし、　　のマイ",
    "ナス表示が１日のへるりょうです。"
  ]},

  # C9: Load 2/2
  0x919C4E: { "b":0x919C4E, "e":0x919C6A, "l":28, "en":"⏫20 C9: Load________2⏮1|/|3__", "ja":"　　搭載コマンドの説明その１"  },
  0x91B70A: { "en":[
    " Assim, cada transporte pode ser",
    " ordenado a embarcar e desembarcar sua",
    " carga quando estiver sobre tipos",
    " específicos de terreno:",
    "____Em qualquer lugar que o { } ande",  # BTP
    "____Não em__________   <ou",            # Heli Transporte
    "____Bancos de areia e Portos",          # Cargueiro
    "____Em qualquer lugar que o { } ande",  # Cruzador
    "____Depósitos"                          # Trem
  ], "ja": [
    "どのユニットに、どのユニットが搭載されるかは",
    "下のひょうをみてください。",
    "",
    "搭載ユニット　　搭載数　　搭載されるユニット",
    "　　列車砲　　　　２　　　地上ユニット　　",
    "　　輸送船　　　　２　　　地上ユニット　　",
    "　　輸送ヘリ　　　１　　　　　　",
    "　　兵員輸送車　　１　　　　　　",
    "　　護衛艦　　　　２　　　　"
  ]},

  # C10: Load 3/3
  0x919C6C: { "b":0x919C6C, "e":0x919C88, "l":28, "en":"⏫20 C10: Load________3⏮1|/|3__", "ja":"　　搭載コマンドの説明その２"  },
  0x91B84E: { "en":[
    " O{||}de qualquer unidade embarcada irá",
    " se ajustar para corresponder as{||}de",
    " seu transporte se for atacado. Isso",
    " ocorre mesmo que nenhum dano real",
    " tenha sido sofrido durante o ataque.",
    #
    # Come back to this one.  There's space for a joke or extra detail.
    #
  ], "ja": [
    "　どのユニットにどこで載れるかは下をみてくだ",
    "さい。",
    "　　　　・・・　　　　　　",
    "　　　　・・・　　　　　　",
    "　　　　・・・　　が移動できる地形　　　",
    "　　　　・・・　　　　　　　　　　　　以外　",
    "　　　　・・・　　が移動できる地形　　　"
  ]},

  # C11: Drop
  0x919C8A: { "b":0x919C8A, "e":0x919CA6, "l":28, "en":"⏫20 C11: Drop____________", "ja":"　　搭載コマンドの説明その３"  },
  0x91B952: { "en":[
    " Com o comando Desembarcar, suas",
    " unidades podem ser descarregadas ao",
    " lado do transporte em qualquer área",
    " disponível. No entanto, a unidade só",
    " pode ser descarregada em terrenos que",
    " ela pode atravessar por conta própria",
    " no campo de batalha."
  ], "ja": [
    "　搭載するがわのユニットの　　がいくつでも搭",
    "載されるがわにえいきょうはありませんが、戦闘",
    "にはいったときに、たとえダメージをうけなくて",
    "も搭載するがわのユニットの　　になります。",
    "　れいをあげると、　　６の輸送ヘリ　　に　　",
    "１０の歩兵　　が載っていたとします。そのまま",
    "戦闘にはいらずに降車できたら　　は１０のまま",
    "ですが、戦闘にはいってしまうとダメージがなく",
    "とも　　６になってしまう、ということです。"
  ]},

  # C12: Wait
  0x919CA8: { "b":0x919CA8, "e":0x919CC4, "l":28, "en":"⏫20 C12: Wait____________", "ja":"　　降車コマンドの説明　　　"  },
  0x91BAFC: { "en":[
    " Embora toda unidade queira que seu",
    " próximo movimento seja o golpe",
    " vencedor, esse sonho não se realiza",
    " todos os dias. Optar por [Aguardar]",
    " simplesmente encerra a vez da unidade",
    " até o próximo dia. Isso conclui seu",
    " treinamento, mas sinta-se à vontade",
    " para revisitar qualquer página ou seção",
    " a qualquer momento. Boa sorte, CO!"
  ], "ja": [
    "　搭載されたユニットが降りるコマンドです。　",
    "　降ろされる場所については、降りるユニットが",
    "移動できる場所ならどこでもいいですが、降ろす",
    "ユニットには、以下のじょうけんがあります。",
    "　　　　・・・　　のみ降車できる",
    "　　　　・・・　　　　のみ降車できる",
    "　　　　・・・　　が移動できる地形　　　",
    "　　　　・・・　　　　　　　　　　　　以外　",
    "　　　　・・・　　が移動できる地形　　　　"
  ]},



# CLEARING STRINGS

  0x91856B: { "b":0x91856B, "e":0x918599, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },
  0x91859D: { "b":0x91859D, "e":0x9185CB, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },
  0x9185CF: { "b":0x9185CF, "e":0x9185FD, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },
  0x918601: { "b":0x918601, "e":0x91862F, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },
  0x918633: { "b":0x918633, "e":0x918661, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },
  0x918665: { "b":0x918665, "e":0x918693, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },
  0x918697: { "b":0x918697, "e":0x9186C5, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },
  0x9186C9: { "b":0x9186C9, "e":0x9186F7, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },
  0x9186FB: { "b":0x9186FB, "e":0x918729, "l":46, "en":"_______________________", "ja":"　　　　　　　　　　　　　　　　　　　　　　　"  },

}
