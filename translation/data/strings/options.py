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

strings = {

  # The sheer number of strings rendered, coupled with the fact that it's not redrawn in
  # its entirety when things change makes it quite tricky not to overwrite tiles still being
  # shown on screen. So we need to explicitly manage tile ranges for everything!

  # If used in other places where explicit VWF buffer position means trouble, make a duplicate of this used only in the game config screen...
  0x8AA77B: { "b":0x8AA77B, "e":0x8AA7AF, "l":52, "en":"⏫00Info.____|_Definir_|___Voltar___|__OK",  "ja":"せつめい　　　きりかえ　　　もどる　　　　　けってい"  },

  # Menu toggle: ○
  0x87DBB8: { "b":0x87DBB8, "e":0x87DBC0, "l":8,  "en":"_⏺C0", "ja":"　○●　"  },
  0x87E29D: { "b":0x87E29D, "e":0x87E2A5, "l":8,  "en":"_⏺C0", "ja":"　○●　"  },
  # Menu toggle: ×
  0x87DBC2: { "b":0x87DBC2, "e":0x87DBCA, "l":8,  "en":"_⏺C1", "ja":"　☆★　"  },
  0x87E2A7: { "b":0x87E2A7, "e":0x87E2AF, "l":8,  "en":"_⏺C1", "ja":"　☆★　"  },

  # Render but not visible?
  #0x87D9FD: { "b":0x87D9FD, "e":0x87DA0F, "l":18, "en":"_BGM         ",  "ja":"　ＢＧＭ　　　　　"  },
  0x87D9FD: { "b":0x87D9FD, "e":0x87DA0F, "l":18, "en":"______",         "ja":"　ＢＧＭ　　　　　"  },


# OPTIONS

  0x87DB40: { "b":0x87DB40, "e":0x87DB52, "l":18, "en":"⏫10_Excluir",         "ja":"　ふさんか　　　　"  },
  0x87DB54: { "b":0x87DB54, "e":0x87DB66, "l":18, "en":"⏫18_Controle__⏺81",  "ja":"　１コントローラー"  },
  0x87DB68: { "b":0x87DB68, "e":0x87DB7A, "l":18, "en":"⏫18_Controle__⏺82",  "ja":"　２コントローラー"  },
  0x87DB7C: { "b":0x87DB7C, "e":0x87DB8E, "l":18, "en":"⏫18_Controle__⏺83",  "ja":"　３コントローラー"  },
  0x87DB90: { "b":0x87DB90, "e":0x87DBA2, "l":18, "en":"⏫18_Controle__⏺84",  "ja":"　４コントローラー"  },
  0x87DBA4: { "b":0x87DBA4, "e":0x87DBB6, "l":18, "en":"⏫20_Computador___",     "ja":"　コンピューター　"  },

  0x87DBE2: { "b":0x87DBE2, "e":0x87DBF4, "l":18, "en":"⏫28_Musica___⏺81_",    "ja":"　おんがく　　１　"  },
  0x87DC6E: { "b":0x87DC6E, "e":0x87DC80, "l":18, "en":"⏫28_Musica___⏺81_",    "ja":"　おんがく　　１　"  },
  0x87DBF6: { "b":0x87DBF6, "e":0x87DC08, "l":18, "en":"⏫28_Musica___⏺82_",    "ja":"　おんがく　　２　"  },
  0x87DC82: { "b":0x87DC82, "e":0x87DC94, "l":18, "en":"⏫28_Musica___⏺82_",    "ja":"　おんがく　　２　"  },
  0x87DC0A: { "b":0x87DC0A, "e":0x87DC1C, "l":18, "en":"⏫28_Musica___⏺83_",    "ja":"　おんがく　　３　"  },
  0x87DC96: { "b":0x87DC96, "e":0x87DCA8, "l":18, "en":"⏫28_Musica___⏺83_",    "ja":"　おんがく　　３　"  },
  0x87DC1E: { "b":0x87DC1E, "e":0x87DC30, "l":18, "en":"⏫28_Musica___⏺84_",    "ja":"　おんがく　　４　"  },
  0x87DCAA: { "b":0x87DCAA, "e":0x87DCBC, "l":18, "en":"⏫28_Musica___⏺84_",    "ja":"　おんがく　　４　"  },
  0x87DC32: { "b":0x87DC32, "e":0x87DC44, "l":18, "en":"⏫28_Musica___⏺85_",    "ja":"　おんがく　　５　"  },
  0x87DCBE: { "b":0x87DCBE, "e":0x87DCD0, "l":18, "en":"⏫28_Musica___⏺85_",    "ja":"　おんがく　　５　"  },
  0x87DC46: { "b":0x87DC46, "e":0x87DC58, "l":18, "en":"⏫28_Musica___⏺86_",    "ja":"　おんがく　　６　"  },
  0x87DCD2: { "b":0x87DCD2, "e":0x87DCE4, "l":18, "en":"⏫28_Musica___⏺86_",    "ja":"　おんがく　　６　"  },
  0x87DC5A: { "b":0x87DC5A, "e":0x87DC6C, "l":18, "en":"⏫28_Musica___⏺87_",    "ja":"　おんがく　　７　"  },
  0x87DCE6: { "b":0x87DCE6, "e":0x87DCF8, "l":18, "en":"⏫28_Musica___⏺87_",    "ja":"　おんがく　　７　"  },
  0x87DBCC: { "b":0x87DBCC, "e":0x87DBE0, "l":20, "en":"⏫28_Musica___⏺C1",      "ja":"　おんがく　　☆★　"  },

  0x87D9E2: { "b":0x87D9E2, "e":0x87D9F4, "l":18, "en":"⏫30_Autoabastece",  "ja":"　オート全補　　　"  },
  0x87E11B: { "b":0x87E11B, "e":0x87E12D, "l":18, "en":"⏫38_Nebl.<de<guerra",    "ja":"　さくてき　　　　"  },
  0x87E136: { "b":0x87E136, "e":0x87E148, "l":18, "en":"⏫40_Subir de nível",      "ja":"　レベルアップ　　"  },
  0x87E151: { "b":0x87E151, "e":0x87E163, "l":18, "en":"⏫48_Dominação",    "ja":"　ゆうせいしょうり"  },
  0x87E187: { "b":0x87E187, "e":0x87E199, "l":18, "en":"⏫50_Batalha rápida",  "ja":"　かんいせんとう　"  },
  0x87E16C: { "b":0x87E16C, "e":0x87E17E, "l":18, "en":"⏫58_Mapa rápido",     "ja":"　こうそくモード　"  },
  0x87E1A2: { "b":0x87E1A2, "e":0x87E1B0, "l":14, "en":"⏫60_Som",         "ja":"　サウンド　　"  },
  0x87E2B1: { "b":0x87E2B1, "e":0x87E2BD, "l":12, "en":"⏫66_Estéreo",        "ja":"　ステレオ　"  },
  0x87E2BF: { "b":0x87E2BF, "e":0x87E2CB, "l":12, "en":"⏫6B__Mono",         "ja":"　モノラル　"  },



# DESCRIPTIONS

  # Fog of war
  0x8AAC54: { "b":0x8AAC54, "e":0x8AAC5E, "l":10, "en":"⏫70_Neblina de guerra",                            "ja":"　さくてき"  },
  0x8AAC60: { "len":46, "org_len":46, "en":[
    "_Quando ativado, a visibilidade do",
    "_inimigo fica limitada a faixa de",
    "_visão de suas unidades."
  ], "ja": [
    "　　ユニットごとに、みえるはんいをもちます。　",
    "　そのはんいのそとは、みえなくなります。"
  ]},

  # Level Up
  0x8AACBC: { "b":0x8AACBC, "e":0x8AACCA, "l":14, "en":"⏫70_Subir de nível",                              "ja":"　レベルアップ"  },
  0x8AACCC: { "len":46, "org_len":46, "en":[
    "_Quando ativado, as unidades ganham",
    "_experiencia durante o combate. O",
    "_poder de ataque é aumentado em 20%",
    "_a cada nível alcançado, e a partir",
    "_do nível 3, o poder de defesa recebe",
    "_o mesmo impulso."
  ], "ja": [
    "　　ユニットが戦闘のたびつよくなるモードです。",
    "　　戦闘をしたユニットにけいけんちがはいり、",
    "　ある一定以上たまるとレベルがあがります。",
    "　　レベルアップすると、攻撃力や守る力がふえ",
    "　ます。"
  ]},

  # Domination
  # "_In addition to destroying all enemy"
  # "_units or capturing an enemy HQ,"
  # "_Domination allows victory if an army"
  # "_occupies at least 75% of all"
  # "_buildings on the map.""

  # "_Domination is, as the name implies,"
  # "_a game of map domination.",
  # "_When enabled, victory is achieved"
  # "_by occupying at least 75% of the"
  # "_buildings on the map."

  # "_Domination is, as the name implies,"
  # "_a game of map domination. Victory",
  # "_is achieved either by capturing an",
  # "_enemy HQ or by occupying at least",
  # "_75% of the buildings on the map.",
  0x8AAD96: { "b":0x8AAD96, "e":0x8AADA8, "l":18, "en":"⏫70_Dominação",                            "ja":"　ゆうせいしょうり"  },
  0x8AADAA: { "len":46, "org_len":46, "en":[
    "_Alem de destruir todas as unidades",
    "_inimigas ou capturar o QG inimigo,",
    "_a Dominação permite a vitória se um",
    "_exercito ocupar pelo menos 75% de",
    "_todas as edificações no mapa."
  ], "ja": [
    "　　敵よりかなりゆうりになったときに、首都占　",
    "　領、または敵を全滅させなくても勝利にするモ",
    "　ードです。　　　　　　　　　　　　　　　　",
    "　　このモードでは占領ポイントの７５％を占領",
    "　すれば勝ちになります。"
  ]},

  # Quick battle
  0x8AAE86: { "b":0x8AAE86, "e":0x8AAE96, "l":16, "en":"⏫70_Batalha rápida",                          "ja":"　かんいせんとう"  },
  0x8AAE98: { "len":40, "org_len":46, "en":[
    "_Quando ativado, batalhas em tela",
    "_cheia são substituídas por breves",
    "_resumos de confronto."
  ], "ja": [
    "　　戦闘の表示をきりかえます。",
    "　　このスイッチを○●にすると、がめんがきり　",
    "　かわらずに、マップ上で戦闘をするようになり",
    "　ます。　　　　　　　　　　　　　　　　　　　"
  ]},

  # Quick map
  0x8AAF4C: { "b":0x8AAF4C, "e":0x8AAF5C, "l":16, "en":"⏫70_Mapa rápido",                             "ja":"　こうそくモード"  },
  0x8AAF5E: { "len":40, "org_len":46, "en":[
    "As unidades se movem rapidamente",
    "no mapa e a exibição de animação",
    "em tela cheia são desativadas."
  ], "ja": [
    "　　このスイッチを○●にするとマップアニメー",
    "　ションとしょうぐんアニメーションがきえます。",
    "　　また、ユニットの移動がはやくなります。　"
  ]},

  # Sound
  0x8AAFEE: { "b":0x8AAFEE, "e":0x8AAFF8, "l":10, "en":"⏫70_Som",                                 "ja":"　サウンド"  },
  0x8AAFFA: { "b":0x8AAFFA, "e":0x8AB020, "l":38, "en":"Seleciona a saída estéreo ou mono.",             "ja":"　ステレオとモノラルをきりかえます。　"  },

  # Player
  0x8AB022: { "b":0x8AB022, "e":0x8AB02E, "l":12, "en":"⏫70_Jogador",                                "ja":"　プレイヤー"  },
  0x8AB030: { "len":40, "org_len":42, "en":[
    "_Seleciona quem controla este",
    "_exército."
  ], "ja": [
    "　　それぞれの軍のプレイヤーをえらびます。",
    "　１コントローラー、２コントローラー、",
    "　コンピューターのせんたくができます。"
  ]},

  # Music
  0x8AB0B0: { "b":0x8AB0B0, "e":0x8AB0BA, "l":10, "en":"⏫70_Musica",                                 "ja":"　おんがく"  },
  0x8AB0BC: { "len":34, "org_len":40, "en":[
    "_Escolha a musica tema do",
    "_exército."
  ], "ja": [
    "　　じぐんのきょくのせんたくをします。　",
    "　プレーヤーは、１ー７までのきょくを　",
    "　えらぶことができます。"
  ]},

  # Auto supply
  0x8AB12C: { "b":0x8AB12C, "e":0x8AB134, "l":8,  "en":"⏫70_Autoabastecer",                           "ja":"　全補給"  },
  0x8AB136: { "len":40, "org_len":34, "en":[
    "_Repara e abastece automaticamente",
    "_unidades em edificações ocupadas",
    "_no início de um novo dia."
  ], "ja": [
    "　　補給モードのせんたくをします。",
    "　全補給を１にちのはじめに自動でするか、　",
    "　コマンドでするかをせんたくします。　"
  ]},



# CO PROFILE

  0x8AA95D: { "b":0x8AA95D, "e":0x8AA973, "l":22, "en":"⏫70|Perfil do CO:",    "ja":"しょうぐんぷろふぃーる"  },
  0x8AA9AB: { "b":0x8AA9AB, "e":0x8AA9B7, "l":12, "en":"⏫78Red Star",       "ja":"レッドスター"  },
  0x8AA9B9: { "b":0x8AA9B9, "e":0x8AA9C7, "l":14, "en":"⏫78Green Earth",    "ja":"グリーンアース"  },
  0x8AA9C9: { "b":0x8AA9C9, "e":0x8AA9D5, "l":12, "en":"⏫78Blue Moon",      "ja":"ブルームーン"  },
  0x8AA9D7: { "b":0x8AA9D7, "e":0x8AA9E7, "l":16, "en":"⏫78Yellow Comet",   "ja":"イエローコメット"  },
  0x8AA9A3: { "b":0x8AA9A3, "e":0x8AA9A9, "l":6,  "en":"⏫78Independente",      "ja":"フリー"  },
  0x8AA9E9: { "b":0x8AA9E9, "e":0x8AA9EF, "l":6,  "en":"⏫78Independente",      "ja":"フリー"  },
  0x8AA9F1: { "b":0x8AA9F1, "e":0x8AA9F7, "l":6,  "en":"⏫78Independente",      "ja":"フリー"  },
  0x8AA985: { "b":0x8AA985, "e":0x8AA98B, "l":6,  "en":"⏫80Nível",          "ja":"レベル"  },
  0x8AA98D: { "b":0x8AA98D, "e":0x8AA991, "l":4,  "en":"⏫88|Memo:",         "ja":"メモ"  },

  # Mr Yamamoto memo
  0x8AA9F9: { "en":[
    "_General lendário que",
    "_comanda um exercito de",
    "_elite incomparável."
  ], "ja": [
    "　ふはいの　でんせつをもつ",
    "　めいしょうぐん　はいかの",
    "　エリートぐんだんはむてき",
  ]},

  # Yuan Delta memo
  0x8AAA51: { "en":[
    "_Um comandante sábio e",
    "_estrategista astuto."
  ], "ja": [
    "　めいしょうぐん",
    "　とってもかしこい"
  ]},

  # Von Rosso memo
  0x8AAA7F: { "en":[
    "_Comandante fervoroso",
    "_com defesa fraca."
  ], "ja": [
    "　せめてせめてせめまくる",
    "　ただし　まもりはよわい"
  ]},

  # Rogenski memo
  0x8AAAB5: { "en":[
    "General médio com",
    "entendimento questionável",
    "do campo de batalha."
  ], "ja": [
    "　じつりょくはふつうだが",
    "　たまにミスをする"
  ]},

  # Hetler memo
  0x8AAAE5: { "en":[
    "⏮1|[Das Volk, mein Schild]",
    "Protege seu povo, mas",
    "é um verdadeiro covarde."
  ], "ja": [
    "　「じんみんはこっかのたて」",
    "　が　くちぐせ",
    "　みかけによらず　きがよわい"
  ]},

  # Caroline memo
  0x8AAB35: { "en":[
    "Apelidada de |[Garota",
    "Sortuda]. Ataca com",
    "forca sem razão aparente."
  ], "ja": [
    "　なんかわからんが　つよい",
    "　あだなは「ラッキーガール」"
  ]},

  # Billy Gates memo
  0x8AAB71: { "en":[
    "_Filho de um bilionário,",
    "_gastando seu dinheiro",
    "_em jogos de guerra."
  ], "ja": [
    "　だいふごうの　むすこで",
    "　ぐんしきんは　ほうふ",
    "　せんそうゲームが　だいすき"
  ]},



# DIPLOMATIC RELATIONS

  0x8BD488: { "b":0x8BD488, "e":0x8BD4BA, "l":50, "en":"⏫c0|Selecionar|Definir|Voltar___||OK",  "ja":"せれくと　　　せっと　　　もどる　　　　　けってい"  },
  0x8BD454: { "b":0x8BD454, "e":0x8BD486, "l":50, "en":"⏫d0_____________|Voltar___||OK",         "ja":"　　　　　　　　　　　　　もどる　　　　　つぎへ　"  },
  0x8BD448: { "b":0x8BD448, "e":0x8BD44C, "l":4,  "en":"⏫18|Aliado",         "ja":"同盟"  },
  0x8BD44E: { "b":0x8BD44E, "e":0x8BD452, "l":4,  "en":"⏫20|Rival",        "ja":"敵対"  },
  0x8BD42C: { "b":0x8BD42C, "e":0x8BD436, "l":10, "en":"⏫28|Jogador",       "ja":"プレイヤー"  },
  0x8BD438: { "b":0x8BD438, "e":0x8BD446, "l":14, "en":"⏫30|Computador",     "ja":"コンピューター"  },
  0x8BD422: { "b":0x8BD422, "e":0x8BD42A, "l":8,  "en":"⏫38|Excluído",     "ja":"ふさんか"  },

}
