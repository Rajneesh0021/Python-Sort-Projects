from  time import  *
import random as r

def mistake(para,test):
    errors=0
    for i in range(len(para)):
        try:
         pass
         if para[i]!=test[i]:
            errors+=1
        except:
            errors=errors+1
    return errors

def speed(time1,time2,test):
   f_time=time2-time1
   time_r=round(f_time,2)
   speed= len(test)/time_r
   return round(speed)


test=['OME children were at play in their play-ground one day, when a herald rode through the town, blowing a trumpet, and crying aloud, "The King! the King passes by this road to-day. Make ready for the King!" The children stopped their play, and looked at one another.','"Did you hear that?" they said. "The King is coming. He may look over the wall and see our playground; who knows? We must put it in order." The playground was sadly dirty, and in the corners were scraps of paper and broken toys, for these were careless children. But now, one brought a hoe, and another a rake, and a third ran to fetch the wheelbarrow from behind the garden gate. They labored hard, till at length all was clean and tidy.','"Now it is clean!" they said; "but we must make it pretty, too, for kings are used to fine things; maybe he would not notice mere cleanness, for he may have it all the time." Then one brought sweet rushes and strewed them on the ground; and others made garlands of oak leaves and pine tassels and hung them on the walls; and the littlest one pulled marigold buds and threw them all about the playground, "to look like gold," he said.','When all was done the playground was so beautiful that the children stood and looked at it, and clapped their hands with pleasure. "Let us keep it always like this!" said the littlest one; and the others cried, "Yes! yes! that is what we will do."']

selected_para=r.choice(test)

print("*******==TYPING TEST==*******")
print(selected_para)
print()
time1=time()
testinput=input("START TYPING: ")
time2=time()

print( "ERRORS: ", mistake(selected_para,testinput))
print("SPEED: ", speed(time1,time2,testinput),"w/sec")
