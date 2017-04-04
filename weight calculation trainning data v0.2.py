#  This part count every feature in each data row
#  for every feature in the file, it should be a 2-dimension list, row: 
#  number of the trainning data, column: weight of every feature.
#  Weidi.Zhang 11/21/2015
#  Feel free to copy, just showing the resource.


import math   # This will import math module


result=[]
row_data =0

feature_num=0 
f=open('e:/result.txt')
for line in f:
    word=list(line.split())
    result.append(word[1:])   # delete the tweeter_id and result

f.close()


#print result
#########   feature1: Team Name  #########	
tmp=[]
tmp2=[]
count1=0
for id in result:           
	for word in id:
		if word=='celtics'or word=='nets'or word=='knickerbockers'\
		or word=='76ers 'or word=='raptors'or word=='cavaliers'\
		or word=='pistons'or word=='pacers'or word=='bucks'\
		or word=='hawks'or word=='bobcats'or word=='heat'\
		or word=='magic'or word=='wizards'or word=='mavericks'\
		or word=='rockets'or word=='hornets'or word=='grizzlies'\
		or word=='spurs'or word=='nugget'or word=='timberwolves'\
		or word=='trailblazers'or word=='supersonics'or word=='jazz'\
		or word=='warriors'or word=='clippers'or word=='lakers':
			count1=count1+1
	row_data=row_data+1		
	tmp.append(count1)
	count1=0
	      
		  
tmp2.append(tmp)

#########   feature2: venue  #########
tmp=[]
count1=0
for id in result:           
	for word in id:
		if word=='fleet'or word=='center'or word=='continental'\
		or word=='airline 'or word=='arena'or word=='madison'\
		or word=='square'or word=='garden'or word=='first'\
		or word=='union'or word=='center'or word=='air'\
		or word=='canada'or word=='centre'or word=='united'\
		or word=='gund'or word=='arena'or word=='palace'\
		or word=='auburn'or word=='hills'or word=='market'\
		or word=='square'or word=='bradley'or word=='philips'\
		or word=='bobcats'or word=='airlines'or word=='td'\
		or word=='waterhouse'or word=='mci'or word=='toyota'\
		or word=='orleans'or word=='sbc'or word=='pepsi'\
		or word=='target'or word=='rose'or word=='garden'or word=='staples'\
		or word=='key'or word=='delta'or word=='oakland':
			count1=count1+1
	tmp.append(count1)
	count1=0
	
tmp2.append(tmp)



#########   feature3: player name  #########
tmp=[]
count1=0
for id in result:           
	for word in id:
		if word=='anthony'or word=='carmelo'or word=='allen'\
		or word=='ray 'or word=='tony'or word=='artest'\
		or word=='carlos'or word=='bosh'or word=='chris'\
		or word=='bryant'or word=='kobe'or word=='bell'\
		or word=='butler'or word=='bynum'or word=='bogut'\
		or word=='chandler'or word=='tyson'or word=='duncan'\
		or word=='tim'or word=='deng'or word=='luol'\
		or word=='gordan'or word=='gasol'or word=='griffin'\
		or word=='josh'or word=='iguodala'or word=='andre'\
		or word=='iverson'or word=='allen'or word=='james'\
		or word=='lebron'or word=='mike'or word=='eddie'\
		or word=='jones'or word=='kirilenko'or word=='kukoc'\
		or word=='lee'or word=='nowitzki'or word=='neal'\
		or word=='jermaine'or word=='pierce'or word=='paul'\
		or word=='parker'or word=='tony'or word=='nathaniel'\
		or word=='cole'or word=='norris'or word=='curry'\
		or word=='stephen'or word=='davis'or word=='kevin'\
		or word=='durant'or word=='garneet'or word=='george'\
		or word=='paul'or word=='hill'or word=='ibaka'\
		or word=='love'or word=='thompson'or word=='klay'\
		or word=='young':
			count1=count1+1
	tmp.append(count1)
	count1=0
	
tmp2.append(tmp)



#########   feature4: terminology  #########
tmp=[]
count1=0
for id in result:           
	for word in id:
		if word=='slam'or word=='dunk'or word=='shot'\
		or word=='fade'or word=='away'or word=='hook'\
		or word=='jump'or word=='rebound'or word=='layup'\
		or word=='perimeter'or word=='block'or word=='three'\
		or word=='point'or word=='assist'or word=='defensive'\
		or word=='field'or word=='goal'or word=='free'\
		or word=='throw'or word=='offensive'or word=='turnover'\
		or word=='mid'or word=='court'or word=='net'\
		or word=='painted'or word=='area'or word=='double'\
		or word=='dribble'or word=='foul'or word=='first'\
		or word=='half'or word=='second'or word=='jump'\
		or word=='ball'or word=='overtime'or word=='substitute'\
		or word=='technical'or word=='second'or word=='gm'\
		or word=='pg'or word=='pf'or word=='rookie'\
		or word=='shooting'or word=='guard'or word=='sixth'\
		or word=='sf'or word=='forward'or word=='losing'\
		or word=='streak'or word=='home'\
		or word=='guest':
			count1=count1+1
	tmp.append(count1)
	count1=0
	
tmp2.append(tmp)



#########   feature5: Pronoun  #########	
tmp=[]
count1=0
for id in result:           
	for word in id:
		if word=='i'or word=='you'or word=='he'or word=='she':
			count1=count1+1	
	tmp.append(count1)
	count1=0
	      
		  
tmp2.append(tmp)


#########   feature6: Weater  #########	
tmp=[]
count1=0
for id in result:           
	for word in id:
		if word=='sunny'or word=='cold'or word=='hot':
			count1=count1+1		
	tmp.append(count1)
	count1=0
	      
		  
tmp2.append(tmp)



#########   feature7: mood  #########	
tmp=[]
count1=0
for id in result:           
	for word in id:
		if word=='exciting'or word=='happy'or word=='thrill'\
		or word=='sad'or word=='angry'or word=='jazz':
			count1=count1+1		
	tmp.append(count1)
	count1=0
	      
		  
tmp2.append(tmp)

#########   feature8: body condition  #########	
tmp=[]
count1=0
for id in result:           
	for word in id:
		if word=='dehydrant'or word=='exhausting'or word=='tired':
			count1=count1+1		
	tmp.append(count1)
	count1=0
	      
		  
tmp2.append(tmp)




#########   feature9: normal adjective  #########	
tmp=[]
count1=0
for id in result:           
	for word in id:
		if word=='nice'or word=='good'or word=='terrible'\
                or word=='bad'or word=='fierce'or word=='best'\
		or word=='every':
			count1=count1+1	
	tmp.append(count1)
	count1=0
	      
		  
tmp2.append(tmp)



#########   feature10: others  #########	
tmp=[]
count1=0
for id in result:           
	for word in id:
		if word=='match'or word=='game'or word=='feel'\
                or word=='bad'or word=='bad':
			count1=count1+1		
	tmp.append(count1)
	count1=0
	      
		  
tmp2.append(tmp)

#########   feature11: verb-self  #########	
tmp=[]
count1=0
for id in result:           
	for word in id:
		if word=='play'or word=='win'or word=='injury'\
                or word=='hurt' or word=='beat':
			count1=count1+1		
	tmp.append(count1)
	count1=0
	      
		  
tmp2.append(tmp)


#########   feature12: verb-others  #########	
tmp=[]
count1=0
for id in result:           
	for word in id:
		if word=='see'or word=='retire'or word=='go'\
		or word=='win' or word=='injury' or word=='watch'\
		or word=='beat':
			count1=count1+1		
	tmp.append(count1)
	count1=0
	      
		  
tmp2.append(tmp)




#########   feature13: adj-others  #########	
tmp=[]
count1=0
for id in result:           
	for word in id:
		if word=='expensive'or word=='after'or word=='cheap'\
		or word=='reasonalbe':
			count1=count1+1	
	tmp.append(count1)
	count1=0
	      
		  
tmp2.append(tmp)




#########   feature14: adj-others  #########	
tmp=[]
count1=0
for id in result:           
	for word in id:
		if word=='home'or word=='tv'or word=='shoe'\
		or word=='ankle'or word=='teammate':
			count1=count1+1		
	tmp.append(count1)
	count1=0
	      
		  
tmp2.append(tmp)



#########   feature15: noun-others  #########	
tmp=[]
count1=0
for id in result:           
	for word in id:
		if word=='ticket'or word=='league'or word=='broadcast'\
		or word=='ankle'or word=='referee'or word=='park'\
		or word=='kid'or word=='nba':
			count1=count1+1		
	tmp.append(count1)
	count1=0
	      
		  
tmp2.append(tmp)














########
# Part 2:
#######  This part count the total number of every feature in each data row


# feature1: Team Name 
total_List=[]
total=0
for id in result:
    for word2 in id:
        if word2=='celtics'or word2=='nets'or word2=='knickerbockers'\
        or word2=='76ers'or word2=='raptors'or word2=='cavaliers'\
	or word2=='pistons'or word2=='pacers'or word2=='bucks'\
	or word2=='hawks'or word2=='bobcats'or word2=='heat'\
	or word2=='magic'or word2=='wizards'or word2=='mavericks'\
	or word2=='rockets'or word2=='hornets'or word2=='grizzlies'\
	or word2=='spurs'or word2=='nugget'or word2=='timberwolves'\
	or word2=='trailblazers'or word2=='supersonics'or word2=='jazz'\
	or word2=='warriors'or word2=='clippers'or word2=='lakers':  
            total=total+1
		        
total_List.append(total)





#feature 2  venue
total=0
for id in result:
	for word2 in id:
		if word2=='fleet'or word2=='center'or word2=='continental'\
		or word2=='airline'or word2=='arena'or word2=='madison'\
		or word2=='square'or word2=='garden'or word2=='first'\
		or word2=='union'or word2=='center'or word2=='air'\
		or word2=='canada'or word2=='centre'or word2=='united'\
		or word2=='gund'or word2=='arena'or word2=='palace'\
		or word2=='auburn'or word2=='hills'or word2=='market'\
		or word2=='square'or word2=='bradley'or word2=='philips'\
		or word2=='bobcats'or word2=='airlines'or word2=='td'\
		or word2=='waterhouse'or word2=='mci'or word2=='toyota'\
		or word2=='orleans'or word2=='sbc'or word2=='pepsi'\
		or word2=='target'or word2=='rose'or word2=='garden'or word2=='staples'\
		or word2=='key'or word2=='delta'or word2=='oakland':
			total=total+1

total_List.append(total)


#feature 3  player name
total=0
for id in result:
	for word2 in id:
		if word2=='anthony'or word2=='carmelo'or word2=='allen'\
		or word2=='ray'or word2=='tony'or word2=='artest'\
		or word2=='carlos'or word2=='bosh'or word2=='chris'\
		or word2=='bryant'or word2=='kobe'or word2=='bell'\
		or word2=='butler'or word2=='bynum'or word2=='bogut'\
		or word2=='chandler'or word2=='tyson'or word2=='duncan'\
		or word2=='tim'or word2=='deng'or word2=='luol'\
		or word2=='gordan'or word2=='gasol'or word2=='griffin'\
		or word2=='josh'or word2=='iguodala'or word2=='andre'\
		or word2=='iverson'or word2=='allen'or word2=='james'\
		or word2=='lebron'or word2=='mike'or word2=='eddie'\
		or word2=='jones'or word2=='kirilenko'or word2=='kukoc'\
		or word2=='lee'or word2=='nowitzki'or word2=='neal'\
		or word2=='jermaine'or word2=='pierce'or word2=='paul'\
		or word2=='parker'or word2=='tony'or word2=='nathaniel'\
		or word2=='cole'or word2=='norris'or word2=='curry'\
		or word2=='stephen'or word2=='davis'or word2=='kevin'\
		or word2=='durant'or word2=='garneet'or word2=='george'\
		or word2=='paul'or word2=='hill'or word2=='ibaka'\
		or word2=='love'or word2=='thompson'or word2=='klay'\
		or word2=='young':
			total=total+1

total_List.append(total)



#feature 4  terminology
total=0
for id in result:
	for word2 in id:
		if word2=='slam'or word2=='dunk'or word2=='shot'\
		or word2=='fade'or word2=='away'or word2=='hook'\
		or word2=='jump'or word2=='rebound'or word2=='layup'\
		or word2=='perimeter'or word2=='block'or word2=='three'\
		or word2=='point'or word2=='assist'or word2=='defensive'\
		or word2=='field'or word2=='goal'or word2=='free'\
		or word2=='throw'or word2=='offensive'or word2=='turnover'\
		or word2=='mid'or  word2=='area'or word2=='double'\
		or word2=='dribble'or word2=='foul'or word2=='first'\
		or word2=='half'or word2=='second'or word2=='jump'\
		or word2=='ball'or word2=='overtime'or word2=='substitute'\
		or word2=='technical'or word2=='second'or word2=='gm'\
		or word2=='pg'or word2=='pf'or word2=='rookie'\
		or word2=='shooting'or word2=='guard'or word2=='sixth'\
		or word2=='sf'or word2=='forward'or word2=='losing'\
		or word2=='streak'or word2=='home'or word2=='guest':		
			total=total+1

total_List.append(total)


#feature 5  pronoun
total=0
for id in result:
	for word2 in id:
		if word2=='i'or word2=='you'or word2=='he'or word2=='she'\
                or word2=='they'or word2=='them'or word2=='we'or word2=='our':
			total=total+1

total_List.append(total)


#feature 6  weather
total=0
for id in result:
	for word2 in id:
		if word2=='sunny'or word2=='cold'or word2=='hot':
			total=total+1

total_List.append(total)


#feature 7  mood
total=0
for id in result:
	for word2 in id:
		if word2=='exciting'or word2=='happy'or word2=='thrill'or word2=='sad'\
                or word2=='angry':
			total=total+1

total_List.append(total)


#feature 8  body condition
total=0
for id in result:
	for word2 in id:
		if word2=='dehydrant'or word2=='exhausting'or word2=='tired':
			total=total+1

total_List.append(total)



#feature 9  normal adjective
total=0
for id in result:
	for word2 in id:
		if word2=='nice'or word2=='good'or word2=='terrible'\
                or word2=='bad'or word2=='fierce'or word2=='best'\
                or word2=='every':
			total=total+1

total_List.append(total)



#feature 10  others
total=0
for id in result:
	for word2 in id:
		if word2=='match'or word2=='game'or word2=='feel'\
		or word2=='posture'or word2=='without'or word2=='weekend':
			total=total+1

total_List.append(total)


#feature 11 verb-self
total=0
for id in result:
	for word2 in id:
		if word2=='play'or word2=='win'or word2=='injury'\
                or word2=='hurt'or word2=='beat'   :
			total=total+1

total_List.append(total)


#feature 12 verb-others
total=0
for id in result:
	for word2 in id:
		if word2=='see'or word2=='retire'or word2=='go'\
                or word2=='win'or word2=='injury'or word2=='watch'\
                or word2=='beat':
			total=total+1

total_List.append(total)


#feature 13 adj-others
total=0
for id in result:
	for word2 in id:
		if word2=='expensive'or word2=='after'or word2=='cheap'\
                or word2=='reasonable':
			total=total+1

total_List.append(total)


#feature 14 noun-self
total=0
for id in result:
	for word2 in id:
		if word2=='home'or word2=='tv'or word2=='shoe'\
                or word2=='ankle'or word2=='teammate':
			total=total+1

total_List.append(total)


#feature 15 noun-others
total=0
for id in result:
	for word2 in id:
		if word2=='ticket'or word2=='league'or word2=='broadcast'\
                or word2=='ankle'or word2=='referee'or word2=='park'\
                or word2=='kid'or word2=='nba':
			total=total+1

total_List.append(total)




####  calculate the weight

for i in total_List:
        feature_num=feature_num+1
        


print feature_num, row_data
#print tmp2
print total_List

weight=[]  # the list which will be sotred into the database
tmp=[]
for i in range(0,feature_num):
    for j in range(0,row_data):
        if tmp2[i][j]==0:
            tmp.append(0)
        else:
            tmp.append(tmp2[i][j]*math.log(total_List[i]))
    weight.append(tmp)
    tmp=[]
            
	    
print weight  # every row contain the number of feature data

#### write the weight
w=open("e:/weight.txt",'wb')   # create the weight file, write the weight



for i in range(0, row_data):
    w.write(str(result[i][0]))
    w.write(str('\t'))
    for j in range(0, feature_num):
        w.write(str(weight[j][i]))
        w.write(str('\t'))
    w.write(str('\n'))
     
w.close()






    
	
