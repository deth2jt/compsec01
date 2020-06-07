letters="theshadowofthemoonsweptacrosstheglobefromhongkongtothetexaspanhandleasarareannularsolareclipsebeganmondaymorninginasiaandtraversedthepacificthesunappearedasathinringbehindthemoontopeopleinanarrowpathalongthecenterofthetrackwhichbeganinsouthernchinaheavycloudsobscuredtheviewinhongkongbutresidentsoftokyoandothercitieswereabletogetaspectacularviewforaboutfourminutesaroundseventhirtytwoammondaysixthirtytwopmetsundayeventswereheldatschoolsandmuseumsinjapanwhilemanymorepeopletookintheunusualastronomicaleventathomeoronstreetcornersafterwhizzingacrossthepacifictheshadowemergedovernortherncaliforniaandsouthernoregonwherethousandsofpeopleattendedpartiestowatchtheeventthefirsttoappearintheunitedstatessincenineteenninetyfourexpertswarnedthathopefulviewersshouldnotpeerupattheskywithoutspecialviewingequipmentsincelookingatthesunwiththenakedeyecancauseblindnessderekralstonaprofessionalphotographersaidheusedaweldingfiltertocaptureadirectviewofeclipseinthefoothillsaboveorovillecaliforniahesharedthephotooncnnireportnotingtheratherslimswathoftheglobewhocouldseetheimpactoftheeclipseralstonsaidhewantedtoenabletherestoftheworldtoseehowclearitlookedtothoseofuswhowerefortunateenoughtoseeitthesliverofsunshinethentraveledsoutheastacrosscentralnevadasouthernutahandnorthernarizonaandthennewmexicoitpassedoveralbuquerquenewmexicoaboutseventhirtyfourpmninethirtyfourpmetbeforepeteringouteastoflubbocktexasaccordingtonasa"

one = ""
zero = ""
two = ""
four = ""
three = ""

for x in range(len(letters)):
    if(x % 5 == 0):
        one += letters[x]
    elif(x % 5 == 1):
        zero += letters[x]
    elif(x % 5 == 2):
        two += letters[x]
    elif(x % 5 == 3):
        four += letters[x]
    elif(x % 5 == 4):
        three += letters[x]
    else:
        "pass"

print("len", len(letters))
#val = len(zero)+ len(one) + len(two) +  len(three) + len(four)
print("len2", len(zero)+ len(one) + len(two) +  len(three) + len(four))

print("zero", zero)
print("one", one)
print("two", two)
print("three", three)
print("four", four)


letters2="hdtopoeehotxnlrnrrpgnogitrhihararetoeiraoeehccaornvusdihotdoyocsaosarfouurstymatymnvweslmmaharpohssoltmnenfhnoefeorvrnfaorgeodeadrtcetrareetnnntrrrhpvrutuhwucigpslnhwhecuisespsatpauwntcrrieshtseiareepoirieemheeoeiteplseentshleciktoheueheeeunneoareldtuntanteipdaueeastypetrberutbtadotafoerhbmkoeadaaaaieomnsdetctnasnbdopeaplhttaigseiaobevnkuiskdreetatawbonadntadxtpueshtodujwmoootuananooerawirhihdeooriiseehhnpenastetioahtaiieeueatoleoortyoevniteitntkealerlaenoaseailouivfptolvvcohreonothhithbcsechianhteeetrswrooewrtegehvsievseccaaunarnodnxterqumotntrnrutreosuksrtaeohntsgfonhaheansesadriarsefepetihhnonrtncrekhnunaydcteonrefotiwbgpcvourtoehtmyhtedeelcsuspinelkeutmeaestetigspiswgetcoaunorusotetohvhspiudecenyetnaeislppeitieemiogeiedasnsktrslohisegeaeeeceehaollnsdhnrtnrrsogwuemoessawdahtedeltehfofnntisrnetlusonnahtdhrahwcaolenxbehfmtypepitobecinhomwctoogttpnselllbmyianvdacueaignmolnwatnfrhenhheloreigbstoneiretcleafisneronirosyteaonennemetnnlocehrrosrzctctamdnelndhrwtaflepeahnftetitsnenopwdhuwhnetkhpliuncktuhaycbneanfohrrhddittdtoinolooefaahtnpottlatoodhatlrodnolrfoooaotssertustifhhadhasrvorhorznneiseuqwcueruiioeotgalcaogsswesaslrngesaaruocenannaaepispdhnietpaohgeotwbitchcsuhwngentahteleeuirtmeuviwosiwtanrdhasialypeiuarivtotcrezasacheerharntonesoptdiwteetpnnssetifxsetfesdeastsawqenoastneneddrooipgedelfrpacwlifibrliihtocengaswflhltpfcetiatbeowtheldouwoaootlostrettsteseaneiaemosvbreiovionhfmfenefoxcna"

val = ord('z') - ord('a') 

def freq(letta):
    #print("DclKDSh", letta)
    for x in range(val+1):
        offset=97
        print(chr(offset+x), letta.count( chr(offset+x)))
        #print( letta.count( chr(offset+x)))
print("fofofof")
freq(letters2)

letters3="theshadowofthemoonsweptacrosstheglobefromhongkongtothetexaspanhandleasarareannularsolareclipsebeganmondaymorninginasiaandtraversedthepacificthesunappearedasathinringbehindthemoontopeopleinanarrowpathalongthecenterofthetrackwhichbeganinsouthernchinaheavycloudsobscuredtheviewinhongkongbutresidentsoftokyoandothercitieswereabletogetaspectacularviewforaboutfourminutesaroundseventhirtytwoammondaysixthirtytwopmetsundayeventswereheldatschoolsandmuseumsinjapanwhilemanymorepeopletookintheunusualastronomicaleventathomeoronstreetcornersafterwhizzingacrossthepacifictheshadowemergedovernortherncaliforniaandsouthernoregonwherethousandsofpeopleattendedpartiestowatchtheeventthefirsttoappearintheunitedstatessincenineteenninetyfourexpertswarnedthathopefulviewersshouldnotpeerupattheskywithoutspecialviewingequipmentsincelookingatthesunwiththenakedeyecancauseblindnessderekralstonaprofessionalphotographersaidheusedaweldingfiltertocaptureadirectviewofeclipseinthefoothillsaboveorovillecaliforniahesharedthephotooncnnireportnotingtheratherslimswathoftheglobewhocouldseetheimpactoftheeclipseralstonsaidhewantedtoenabletherestoftheworldtoseehowclearitlookedtothoseofuswhowerefortunateenoughtoseeitthesliverofsunshinethentraveledsoutheastacrosscentralnevadasouthernutahandnorthernarizonaandthennewmexicoitpassedoveralbuquerquenewmexicoaboutseventhirtyfourpmninethirtyfourpmetbeforepeteringouteastoflubbocktexasaccordingtonasa"


def subst(letta, shift):
    letters4=""
    for x in range(len(letta)):
        #shift = 10
        letters4 += chr(    (ord(letta[x]) - ord('a') - shift) % 26 + ord('a'))
    return letters4

letters4 = subst(letters3, 10)
print("O_Caesar: ", letters3)
print("Caesar: ", letters4)
print("letters4Caesar freq")
freq( letters4)


letters5="wyctlgjlfkieybrsyjdiepnvryfyczjuaiigmyeuooqcpfnvthfwyszmryiqnmpzmffqnaybkmgtlvjmqjhvllnycalgbycbsjvhnhwyfyuexuaijetxhhyexuyqisybrrvnxyqthvqfrluyqsbgnnnhrijetjrwnltzfthlybnyqnxbnheriuaizrswrivlhlvrcaffffjcflrsnydqbwevsastlatlgmebwynxghwxrwihxxvhnnyiexbvumbsscnwgzlrxyayyeyuvsgrsnjfminwgngveyqwypjhgqsvsuzfdbwwbwjbwugjmrhoennlglrfwufjcflrsnydcawygffvfnvthstlgmyhuwbrcalwbryqdnujcayyeacrbxvlcgffptjvjmbkoawyyjufjxsnfzxjrwmbsuykcafhpnuyiugfiajhgjlgfcaryaycaiofyllsigfvyjmrruvqmcfmfbieimnsxbybrwcakierugniaflruieyyqthrmoailrinrwuodnrxisiugfcaffymuijvrjhfyiyjhngihyzbzlgdavluodnrxbnayojyaruqjjhgfvhmbkueruvsmgwynrjhgfvhugniaxqunwuflrsyijlejnvhyayuotogxwbqxvsayjmfjmgfvynmujxzjxvfiijlnwwnsywtoesuynmgnwfhlhufrxuejjhgfvxbvsaqfgnlcalxnyuswizybvxnetprfmajqfuucjlffhqsyjxwufhajffhuyqnujmgtfrsmbssqfnnbcgmaejugwyynmufhqguejflhiahynqyqhiayyzunstlutfydqbtxgmyajqltlxyczjmvxmuflvsahswuflvyuoqyptgzjhgxgniyvsyzfcyxvryqrjhgmyrcnefieicaflvqsfzwpjmfkoyulbiopjlfhigylhicafhqxiadmgzxvtwbhbnnljtgnsuzdjnxwnqnujqnxbvsagthctmgjgcmufntrxnufnezxvsbnioapcaiqbwxfkieulbrcajhgfwgwyfxxvwypyiefhqulbiopjlnsarqcafdbqcrfmjjfyfmstlnscyqwbswrnprijyfhgtvhnfqfwyjicfnefgbacrflbzhqoiynygngrrutftvsyfxuzklveyyqnrfmrxnujmrayarifyihylnlybzmgmcalmjjfrflajxswizybrxiadbnheswcmjfyiypqcajxgtlrxjbsxgtkhjmgniaxzetgafnvthnqlracrbiaqcajuotogybrulbulvjnltzgwuskcppcalcaxnbqyalibimstlgmyczlctmrtzjwcgnhtglrfnuqyfxueycpqyffvbznfhogyfrgogynufnvkcgnhitfijxnssbybrwcaiofyllbihqxojwbsmviyejxjjfybcgmcaybrgihsxnwcrxissieruybiepjyfwrxhvucaluyxiqjwynhvsagtwbrgrsnznwufyyhcruflfhqglbtefguesyftzgmygngrxuaipnwcrysfffrcmgjxzfhnbufmcalnbsjbxnricgtlejmcthqxnufngmycfjrwxbjmatncjlznnejjbwnrwmgtvejuxybrqujnhczlfzcgtzfyienyfbyajprwyahihwutjuadiajnbxnrffqtwhryaymafnvthnqypthbrsnsxozmvsyfxyqnnbwaejafhbajcqjljwcgjmvsuajgnnfgthnycbsuywyinyjthynhrmijjprwqujhqtwhryaymzferybrnljfsvsnbybruooqcpiizfcatlnwyfjhgyihxqrflrbcgmcatoewctmnfyiejjbwnbsnujgyjuxxzetgptgcfhvjmnsxttprwhzjhgfarswvjmnwyatnhswbrgbsiijlzfhliypfxrxmhhbyjuxxbnaycwyfjhgjxajqftltfhveugniaxqvybnbcqjlnsartzpnlpzgfyuahyfybnywnqfstlgmyzyircyehcfjdhiazjhgbynxmrxmrfwuxygtzsfwgxcaicinxhffydcaybvxcaxnnswrybrwyyjufjisiipzgrsnfbuffhrayaynufnqjgnsxriwbayefarfhqybrnhstlzfnvthowihlbgyiynauybnxmgnlejxqnmpzmfniafvbznnmifyisqytnnvrugjcfxorxnufnnqmbbuewuayyqhiijlnly"
#letters5="wyctlgjlfkieybrsyjdiepn"
#http://www.simonsingh.net/The_Black_Chamber/vigenere_cracking_tool.html
key_length = 3

set1=""
set2=""
set3=""

for x in range(len(letters5)):
    if(x % 3 == 0):
        set1 += letters5[x]
    elif(x % 3 == 1):
        set2 += letters5[x]
    elif(x % 3 == 2):
        set3 += letters5[x]
    else:
        "pass"

print("set1 freq")
print("set1 ", set1)
freq( set1)
print("set2 freq")
print("set2 ", set2)
freq( set2)
print("set3 freq")
print("set3 ", set3)
freq( set3)

val1 = ord('j') - ord('e')
set1 = subst(set1, val1)
val2 = ord('y') - ord('e')
set2 = subst(set2, val2)
val3 = ord('r') - ord('e')
set3 = subst(set3, val3)

'''
print("val ", val1)
print("set1after ", set1)

print("set1[0]: bb", (set1))
print("set2[0]: bb", (set2))
print("set3[0]:bb ", (set3))
'''
#maxLen = max()

def foo(set1,set2,set3):
    #count = 0
    foobar = ""
    
    while not (len(set1) == 0 and len(set2) == 0 and len(set3) == 0):
    
        
        if len(set1) == 0 and len(set2) == 0 and len(set3) != 0:
            foobar +=  set3[0]

        elif len(set1) == 0 and len(set2) != 0 and len(set3) != 0:
            foobar += set2[0]+ set3[0] 

        elif len(set1) != 0 and len(set2) == 0 and len(set3) != 0:
            foobar += set1[0]+ set3[0]

        elif len(set1) != 0 and len(set2) != 0 and len(set3) == 0:
            foobar += set1[0]+ set2[0] 

        elif len(set1) != 0 and len(set2) == 0 and len(set3) == 0:
            foobar += set1[0] 

        elif len(set1) == 0 and len(set2) != 0 and len(set3) == 0:
            foobar += set2[0] 
        else:
            foobar += set1[0]+ set2[0]+set3[0] 

        set1 = set1[1:]
        set2 = set2[1:]
        set3 = set3[1:]
        
        #count = count + 1
    return foobar

def checkEmpty(stringVal):
    if stringVal == "":
        return ""
    else:
        return stringVal


print ("plaintext", foo(set1,set2,set3))
#print ("plaintext", foo("abc","123","~?"))


