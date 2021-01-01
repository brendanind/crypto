from functions import boring

plain = boring('''dear uncle Wilhelm as you promised we thoroughly enjoyed our visit to your cousin in lincoln and found it most informative stop 

 the beautiful cathedral almost justified our visit on its own and our hosts shared with us some interesting drawings of the towers you mentioned stop they graciously allowed me to copy the sketches and explained much about how the towers are built and why stop 

 as usual i will send you my notes and sketches via our dear friend jessica who has promised to ensure their safe delivery stop 

 really i must congratulate our hosts in the local scout groups for the marvellous way in which they have organised our travel though some of the scouts have been rather more solicitous than we had expected asking rather a lot of questions about our plans stop 

 generally i hope they were satisfied with the answers that we gave but we feel that we are at risk of overstaying our welcome so we will return to london on tuesday stop 

 eventhough we have enjoyed our time together there has been some debate among the group about where we should visit next stop 

 there are so many interesting sites to visit along the majestic thames estuary so we have decided to split into two groups stop 

 ralf will lead one party on a tour of the kent coast while i am very much looking forward to exploring the essex marshes stop 

 do let me know if you have a better idea but i have been told that canewdons fifteenth century church affords an elevation with a wideview of the surrounding lands in this other wiser at her flat landscape and is the site of another fascinating tower which i will be certain to sketch for you stop 

 finally if you have any further requests for specific information then perhaps you could leave a message for me at the post office there stop karl message ends ''')

enc = "hewzculsefpsoestwajvcxzvtpaehfebovzvcnosjeuqvjehvczdpapbbvjvczlvcapupuspulvsuwuhmvcuhpbtvabpumvztwbpdeabvxboeiewcbpmcslwboehzwswstvabqcabpmpehvczdpapbvupbavfuwuhvczovabaaowzehfpbocaavtepubezeabpunhzwfpunavmboebvfezajvcteubpvuehabvxboejnzwlpvcasjwssvfehtebvlvxjboearebloeawuhegxswpuehtclowivcbovfboebvfezawzeicpsbwuhfojabvxwacacwspfpssaeuhjvctjuvbeawuharebloeadpwvczhewzmzpeuhqeaaplwfovowaxzvtpaehbveuaczeboepzawmehespdezjabvxzewssjptcablvunzwbcswbevczovabapuboesvlwsalvcbnzvcxamvzboetwzdessvcafwjpufoploboejowdevznwupaehvczbzwdesbovcnoavtevmboealvcbaowdeieeuzwboeztvzeavsplpbvcabowufeowhegxelbehwarpunzwboezwsvbvmyceabpvuawivcbvczxswuaabvxneuezwssjpovxeboejfezeawbpampehfpboboewuafezabowbfenwdeicbfemeesbowbfewzewbzparvmvdezabwjpunvczfeslvteavfefpsszebczubvsvuhvuvubceahwjabvxedeubovcnofeowdeeuqvjehvczbptebvneboezboezeowaieeuavteheiwbewtvunboenzvcxwivcbfoezefeaovcshdpapbuegbabvxboezewzeavtwujpubezeabpunapbeabvdpapbwsvunboetwqeabplbowteaeabcwzjavfeowdehelphehbvaxspbpubvbfvnzvcxaabvxzwsmfpsssewhvuexwzbjvuwbvczvmboereublvwabfopsepwtdezjtclosvvrpunmvzfwzhbvegxsvzpunboeeaaegtwzaoeaabvxhvsebteruvfpmjvcowdewiebbezphewicbpowdeieeubvshbowblwuefhvuampmbeeuboleubczjloczlowmmvzhawuesedwbpvufpbowfphedpefvmboeaczzvcuhpunswuhapubopavboezfpaezwboezmswbswuhalwxewuhpaboeapbevmwuvboezmwalpuwbpunbvfezfoplopfpssielezbwpubvareblomvzjvcabvxmpuwssjpmjvcowdewujmczboezzeyceabamvzaxelpmplpumvztwbpvuboeuxezowxajvclvcshsewdewteaawnemvztewbboexvabvmmpleboezeabvxrwzsteaawneeuha"


for i in range(0,len(plain)):


    cy = enc[i]
    print("Encoded: " + str(cy))
    pl = plain[i]
    print("Plain: " + str(pl))
    print("\n")
