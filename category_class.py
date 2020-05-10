# some problem in implementing category3 dictionary
# repeating key because of repeating folders name
from enum import Enum
import re

# define some basic utilities for Enum classes
class CustomEnum(Enum):
  @classmethod
  def describe(cls):
    s = ''
    for c in category1:
        s += "'"+ re.sub(r'(^.+)\.', '', str(c)) + "', "
    return s[:-2]
  
######################################################################  
  
# Enumeration class for category 1
# A-機能分類 (func)
# B-理論分類 (theory)
# C-表現法 (expression)
class category1(CustomEnum):
  func = 1
  theory = 2
  expression = 3
  
  
class category1dict():
  d = {
    '機能分類': category1.func, 
    '理論分類': category1.theory, 
    '表現法': category1.expression,
  }
  
  @staticmethod
  def __getitem__(s):
    return category1dict().d[s]
  
####################################################################  
  
# Enumeration class for category 2
# A1-別墅住宅 (villa)
# A2-集合住宅 (housing)
# A3-辦公室 (office)
# A4-住(辦)(商),夾層,複合,LOFT (condo)
# A5-學校,圖書館,實驗室,老人院 (school)
# A6-展場,GALLERY,古蹟 (gallery)
# A7-旅館,hospital,dom (hotel)
# A8-劇場,體育設施,church (theater)
# A9-停車場,車站,機場,工廠,toilet (parking)
# A10-商業設施 (business)
# A11-urban space(urban)
# B1-細部 (detail)
# B2-結構概念 (structure)
# B3-表現法 (expression_)
# C1-sketch (sketch)
# C2-computer (computer)
# C3-complex (complex)
class category2(CustomEnum):
  A1 = 1; A2 = 2; A3 = 3; A4 = 4; A5 = 5
  A6 = 6; A7 = 7; A8 = 8; A9 = 9; A10 = 10
  A11 = 11; B1 = 12; B2 = 13; B3 = 14; C1 = 15
  C2 = 16; C3 = 17
  
class category2dict():
  d = {
    '別墅住宅': category2.A1,
    '集合住宅': category2.A2,
    '辦公室': category2.A3,
    '住(辦)(商),夾層,複合,LOFT': category2.A4,
    '學校,圖書館,實驗室,老人院': category2.A5,
    '展場,GALLERY,古蹟': category2.A6,
    '旅館,hospital,dom': category2.A7,
    '劇場,體育設施,church': category2.A8,
    '停車場,車站,機場,工廠,toilet': category2.A9,
    '商業設施': category2.A10,
    'urban space': category2.A11,
    '細部': category2.B1,
    '結構概念': category2.B2,
    '表現法': category2.B3,
    'sketch': category2.C1,
    'computer': category2.C2,
    'complex': category2.C3,
  }
  
  @staticmethod
  def __getitem__(s):
    return category2dict().d[s]
  
####################################################################

# Enumeration class for category 3
# A1a-form (for)
# A1b-plan,dwg (pla)
# A1c-Garden-terrace,balcony,green house,swimming,attic (gar)
# A1d-Privacy-foyer,living,dining,BD,closet,study,Kitchen, powder, (pri)       
# A1e-Public-Entr,TYP lobby (pub)
# A2a-Garden-terrace,balcony,green house,swimming (gar)
# A2b-form (for)
# A2c-plan,dwg (pla)
# A2d-Privacy-foyer,living,dining,BD,closet,study,Kitchen, powder,laundry (pri)
# A2e-Public-Entr,TYP lobby (pub)
# A3a-Garden-terrace,lounge (gar)
# A3b-form (for)
# A3c-plan,dwg (pla)
# A3d-meeting,president room, powder, (mee)
# A3e-studio (stu)
# A3f-Public-Entr,TYP lobby (pub)
# A4a-Garden-terrace,balcony,green house,swimming (gar)
# A4b-form (for)
# A4c-plan,dwg (pla)
# A4d-Privacy-foyer,living,dining,BD,closet,study,Kitchen, powder, (pri)
# A4e-Public-Entr,TYP lobby (pub)
# A5a-institution, laboratory,retire,cemetery (ins)
# A5b-public library (pub)
# A5c-form (for)
# A5d-plan,dwg (pla)
# A5e-kindergarten (kin)
# A5f-university,high school (uni)
# A6a-plan,dwg (pla)
# A6b-exhibition (exh)
# A6c-form (for)
# A7a-form (for)
# A7b-restaurant,Garden-terrace,swimming (res)
# A7c-plan,dwg (pla)
# A7d-room,closet, powder, (roo)
# A7e-Public-Entr,TYP lobby (pub)
# A8a-hall, playground (hal)
# A8b-form (for)
# A8c-plan,dwg (pla)
# A8d-lobby, cafe (lob)
# A9a-form (for)
# A9b-sign (sig)
# A9c-plan,dwg (pla)
# A9d-space (spa)
# A9e-external layer (ext)
# A10a-logo, graphic,image,history (log)
# A10b-club,casino,yacht,cinemas (clu)
# A10c-restaurant (res)
# A10d-Japanese spring,spa,gim,pool (jap)
# A10e-retail (ret)
# A10f-show room,bank,接待中心 (sho)
# A10g-fashion (fas)
# A10h-saloon,beauty shop (sal)
# A10i-(lounge)bar,cafe',cellar ((lo)
# A10j-shopping mall,waterfront,playworld (sho)
# B1a-Furniture and fittings,deco (fur)
# B1b-Landscap,paving,deck,floor,drain (lan)
# B1c-Structure,plastic,tent,slab (str)
# B1d-Lifts,mech,AC,heating,venti (lif)
# B1e-door (doo)
# B1f-Canopy, entrance,shelter (can)
# B1g-Wood (woo)
# B1h- Tile ( ti)
# B1i-counter (cou)
# B1j-column (col)
# B1k-Balconies (bal)
# B1l-Bridge,object,fall,pavilion (bri)
# B1m-Lighting (lig)
# B1n-External walls,fence (ext)
# B1o-Rail (rai)
# B1p-ceiling,courtyard (cei)
# B1q-Staircase,ramp (sta)
# B1r-textile (tex)
# B1s-Masonry,concrete,brick,painting (mas)
# B1t-metal,steel,Texture (met)
# B1u-partition,internal wall,path (par)
# B1v-louver,curtain (lou)
# B1w-Roof,solar,wind,skylight,Green (roo)
# B1x-window (win)
# B1y-Stone (sto)
# B1z-Glass (gla)
class category3(CustomEnum):
  A1a = 1;  A1b = 2;  A1c = 3;  A1d = 4;  A1e = 5
  A2a = 6;  A2b = 7;  A2c = 8;  A2d = 9;  A2e = 10
  A3a = 11;  A3b = 12;  A3c = 13;  A3d = 14;  A3e = 15
  A3f = 16;  A4a = 17;  A4b = 18;  A4c = 19;  A4d = 20
  A4e = 21;  A5a = 22;  A5b = 23;  A5c = 24;  A5d = 25
  A5e = 26;  A5f = 27;  A6a = 28;  A6b = 29;  A6c = 30
  A7a = 31;  A7b = 32;  A7c = 33;  A7d = 34;  A7e = 35
  A8a = 36;  A8b = 37;  A8c = 38;  A8d = 39;  A9a = 40
  A9b = 41;  A9c = 42;  A9d = 43;  A9e = 44;  A10a = 45
  A10b = 46;  A10c = 47;  A10d = 48;  A10e = 49;  A10f = 50
  A10g = 51;  A10h = 52;  A10i = 53;  A10j = 54;  B1a = 55
  B1b = 56;  B1c = 57;  B1d = 58;  B1e = 59;  B1f = 60
  B1g = 61;  B1h = 62;  B1i = 63;  B1j = 64; B1k = 65 
  B1l = 66;  B1m = 67;  B1n = 68;  B1o = 69;  B1p = 70
  B1q = 71;  B1r = 72;  B1s = 73;  B1t = 74;  B1u = 75
  B1v = 76;  B1w = 77;  B1x = 78;  B1y = 79;  B1z = 80

class category3dict():
  A1_dict = {
    
  }
  index_dict = {
    'A1': A1_dict
  }
  
  @staticmethod
  def __getitem__(s):
    return 

######################################################################## 
  
# Enumeration class for category 4
# x-art (art)
# y-logic (log)
# z-pop (pop)
class category4(CustomEnum):
  art = 1
  log = 2
  pop = 3

class category4dict():
  d = {
    'art': category4.art,
    'log': category4.log, 
    'pop': category4.pop,
  }
  
  @staticmethod
  def __getitem__(s):
    return category4dict().d[s]

########################################################################
# some conveninet variables when using category_class
categorydict = [category1dict(), category2dict(), category3dict(), category4dict()]