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

  # Map info box
  0x87FB72: { "b":0x87FB72, "e":0x87FB86, "l":20, "en":"Território não reivindicado", "ja":"まだ占領していません"  },
  0x87FB88: { "b":0x87FB88, "e":0x87FB8E, "l":6,  "en":"Conquistado|por",                "ja":"軍占領"  },
  0x87FB90: { "b":0x87FB90, "e":0x87FB98, "l":8,  "en":"Duração⏮1n:",          "ja":"占領日数"  },
  0x87FB9A: { "b":0x87FB9A, "e":0x87FB9C, "l":2,  "en":" dias",                 "ja":"日"  },

  # 2P Classic Maps
  0x83808E: { "b":0x83808E, "e":0x83809E, "l":16, "en":"Ilha Feijão",        "ja":"ソラマメジマ　　"  },
  0x8380A3: { "b":0x8380A3, "e":0x8380B3, "l":16, "en":"Ilha Donut",       "ja":"ドーナツジマ　　"  },
  0x8380B8: { "b":0x8380B8, "e":0x8380C8, "l":16, "en":"Ilhas Onigiri",      "ja":"オニギリジマ　　"  },
  0x8380CD: { "b":0x8380CD, "e":0x8380DD, "l":16, "en":"Ilhas Balão",       "ja":"タマタマジマ　　"  },
  0x8380E2: { "b":0x8380E2, "e":0x8380F2, "l":16, "en":"Lago Coral",       "ja":"マガタマジマ　　"  },
  0x8380F7: { "b":0x8380F7, "e":0x838107, "l":16, "en":"Trio|Puzzle",        "ja":"ハゴロモジマ　　"  },
  0x83810C: { "b":0x83810C, "e":0x83811C, "l":16, "en":"A Península",     "ja":"キメンハントウ　"  },
  0x838121: { "b":0x838121, "e":0x838131, "l":16, "en":"Porto Cervo",        "ja":"ペケジマ　　　　"  },
  0x838136: { "b":0x838136, "e":0x838146, "l":16, "en":"Região Alara",        "ja":"アララサンミャク"  },
  0x83814B: { "b":0x83814B, "e":0x83815B, "l":16, "en":"Rio Perdido",         "ja":"チリヂリガワ　　"  },
  0x838160: { "b":0x838160, "e":0x838170, "l":16, "en":"Ilha Vulcão",       "ja":"ノアカザントウ　"  },
  0x838175: { "b":0x838175, "e":0x838185, "l":16, "en":"Atol<Tartarugas",       "ja":"ツキノワジマ　　"  },
  0x83818A: { "b":0x83818A, "e":0x83819A, "l":16, "en":"Ilha Alongada",      "ja":"ハマキジマ　　　"  },
  0x83819F: { "b":0x83819F, "e":0x8381AF, "l":16, "en":"Chaves Cubo",          "ja":"サイコロジマ　　"  },
  0x8381B4: { "b":0x8381B4, "e":0x8381C4, "l":16, "en":"Ilhas|Espelho",     "ja":"フタゴジマ　　　"  },
  0x8381C9: { "b":0x8381C9, "e":0x8381D9, "l":16, "en":"Estreito do Tubarão",       "ja":"デビラートウ　　"  },
  0x8381DE: { "b":0x8381DE, "e":0x8381EE, "l":16, "en":"Canal Real",      "ja":"ラストドリーム　"  },

  # 2P "New" Maps
  0x8382B1: { "b":0x8382B1, "e":0x8382BB, "l":10, "en":"Ilha Abrupta",       "ja":"コツブジマ"  },
  0x8382C0: { "b":0x8382C0, "e":0x8382CA, "l":10, "en":"Ilha Moji",        "ja":"ピーノシマ"  },
  0x8382CF: { "b":0x8382CF, "e":0x8382DF, "l":16, "en":"Cabo Turbulento",       "ja":"グーチョキミサキ"  },
  0x8382E4: { "b":0x8382E4, "e":0x8382F2, "l":14, "en":"Ponte Visão",      "ja":"メガネオオハシ"  },
  0x8382F7: { "b":0x8382F7, "e":0x838305, "l":14, "en":"Quatro Rios",        "ja":"ヒキョウノモリ"  },
  0x83830A: { "b":0x83830A, "e":0x83831A, "l":16, "en":"Rio Serpente",       "ja":"マウンテンリバー"  },
  0x83831F: { "b":0x83831F, "e":0x83832D, "l":14, "en":"Costa da Mordida",          "ja":"パックンランド"  },
  0x838332: { "b":0x838332, "e":0x83833E, "l":12, "en":"Fim do Mundo",         "ja":"アシナガジマ"  },
  0x838343: { "b":0x838343, "e":0x83834F, "l":12, "en":"Ilha Esperança",        "ja":"チエノワジマ"  },
  0x838354: { "b":0x838354, "e":0x838360, "l":12, "en":"Ilha Tanabata",       "ja":"タナバタジマ"  },
  0x838365: { "b":0x838365, "e":0x838375, "l":16, "en":"Estreito do Punho",     "ja":"コブシカイキョウ"  },
  0x83837A: { "b":0x83837A, "e":0x83838A, "l":16, "en":"Serra Estreita",         "ja":"ハマキサンミャク"  },
  0x83838F: { "b":0x83838F, "e":0x83839F, "l":16, "en":"Ilhas Dispersas",     "ja":"パラパラショトウ"  },
  0x8383A4: { "b":0x8383A4, "e":0x8383B2, "l":14, "en":"Ilhas Ovo",        "ja":"ネコノラクエン"  },
  0x8383B7: { "b":0x8383B7, "e":0x8383C3, "l":12, "en":"Duas Cascatas",          "ja":"クネクネジマ"  },
  0x8383C8: { "b":0x8383C8, "e":0x8383D6, "l":14, "en":"Contagem Regressiva",          "ja":"カウントダウン"    },
  0x8383DB: { "b":0x8383DB, "e":0x8383EB, "l":16, "en":"Batalha Final",       "ja":"ファイナルウォー"  },

  # 4P Special Maps
  0x8381F3: { "b":0x8381F3, "e":0x838201, "l":14, "en":"Cabo Foguete",        "ja":"ロケットミサキ"  },
  0x838206: { "b":0x838206, "e":0x838216, "l":16, "en":"Rio Colheita",         "ja":"ウォーターランド"  },
  0x83821B: { "b":0x83821B, "e":0x838227, "l":12, "en":"Rio Farrapos",       "ja":"ヨレヨレガワ"  },
  0x83822C: { "b":0x83822C, "e":0x838238, "l":12, "en":"Ilhas Rivais",      "ja":"ピーナツジマ"  },
  0x83823D: { "b":0x83823D, "e":0x838249, "l":12, "en":"Alakule",            "ja":"アラクレジマ"  },
  0x83824E: { "b":0x83824E, "e":0x83825A, "l":12, "en":"Ilhas Glória",      "ja":"デロリントウ"  },
  0x83825F: { "b":0x83825F, "e":0x83826D, "l":14, "en":"Lagos Primavera",       "ja":"ダルマハントウ"  },
  0x838272: { "b":0x838272, "e":0x838282, "l":16, "en":"Colinas Fabula",        "ja":"ダルマサンミャク"  },
  0x838287: { "b":0x838287, "e":0x838297, "l":16, "en":"Rio Traiçoeiro",      "ja":"コロコロテツドウ"  },
  0x83829C: { "b":0x83829C, "e":0x8382AC, "l":16, "en":"Cabo Sul",         "ja":"ミナミノラクエン"  },

}
