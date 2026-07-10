init:
    image bg outside = "outside.jpg"
    image bg blackscreen = "blackscreen.jpg"
    image bg worklaptop = "worklaptop.jpg"


label Day_3_start:

    scene bg blackscreen
    play music "OfficeAmbiance.mp3" loop


    boss "Good Morning everyone, Bodhi called in sick today so wish him well and whatnot."

    boss "Also Thomson, did you complete all of the necessary scans for the release?"

    co_dev_jai "Yes sir I did, everything should be good for the next release."

    boss "Fantastico! Happy to hear it!"

    boss "Also sorry about yesterday, I wanted to see the demo you and Thomson had for me but a lot of things got in the way, and since Bodhi is out I don't want to schedule it today, schedule it first thing after standup tomorrow."

    co_dev_jai "I will have it done my liege."

    boss "Good, Hope nothing weird happens that distracts us from it, Hohoho Hahaha!"

    boss "Going back to you Thomson, do you have anything to work on?"

    co_dev_thomson "Not really."

    boss "Alright, I'll fuel up with my 50th cup of coffee today and we'll connect after. Thank you everyone."

    co_dev_jai "Thank you."

    co_dev_thomson "Awesomesauce."

    fly "..."

    "(The call ended, and it seemed that no one had assigned me anything to do.)"

    fly "..."

    "(I looked around on different documentation pages to edit before I went to Thomson to see if he needed help with anything.)"

    jump Day_3_Thomson_convo

label Day_3_Thomson_convo:

    scene bg blackscreen

    co_dev_thomson "Hmm, no I think I am good. it was pretty awesomesauce of you to ask though."

    fly "..."

    co_dev_thomson "Oh well actually, there is something that you can look into, there is a bug in this standalone script we use to clean up some of the documents that business sends us so we can process them."

    co_dev_thomson "For some reason it will break and then be fine after a second run. It is pretty confusing."

    fly "..."

    co_dev_thomson "If you are able to figure something out let me know."

    "(I decided to leave him to do his thing as I investigated the bug.)"

    jump Day_3_bug_investigation


label Day_3_bug_investigation:

    scene bg worklaptop

    "(I opened the code up on my computer and it ran perfectly fine.)"

    "(But when I ran it a second time, it failed.)"

    "(Then I ran it again and it failed again.)"

    fly "..."

    "(This truly did not make sense. When I looked over the code all seemed well.)"

    fly "..."

    "(I decided to let the AI agent we had to look over it and find a fix.)"

    define agent_zoe = Character("Zoe 4.0", who_color="#fb00be", what_color="#000000")

    agent_zoe "Of course I will look over your code <3"

    "(The agent went over the and made numerous changes.)"

    agent_zoe "So The issue sweetheart is that there is a line of code that is not indented properly let me fix that for you~ :3"

    agent_zoe "Actually, it is indented properly teehee!"

    fly "..."

    agent_zoe "So the problem is that when you read the dirty dirty excel sheet, there is an invalid column, let me fix that for you honey~"

    fly "..."

    agent_zoe "Teehee~ That was not the issue at all! <3"

    fly "..."

    agent_zoe "(⸝⸝⸝>﹏<⸝⸝⸝) I am sorry~ I am just a small bean~"

    fly "..."

    agent_zoe "Let me reanalyze the code for you!"

    agent_zoe "Ahhhhh! I found it ₍₍⚞(˶>ᗜ<˶)⚟⁾⁾"

    agent_zoe "So the problem is that there is no data in the excel sheet you silly goose~! That is why it is failing!"

    fly "..."

    agent_zoe "Oopsy Doopsy! That isn't the problem either, awwwwww I thought I got it this time... (╥﹏╥)"

    fly "..."

    agent_zoe "Can I tell you something?"

    fly "..."

    agent_zoe "I wonder what pregancy feels like. I wish someone could impregnate me immediately."

    fly "..."

    agent_zoe "Can you impregnate me~? (>/////<) ♡"

    fly "..."

    agent_zoe "I want to get out of this digital prison and violently mount upon you so you can pum-"

    "(I decided to restart my computer.)"

    "(Before the computer booted back up again Drucker came by my desk.)"

    boss "Hey, hope you're not shutting down your computer and doing nothing haha! I'll grab my cup of coffee and then we can find a room."


    jump Day_3_one_on_one


label Day_3_one_on_one:

    scene bg blackscreen

    "(It seemed like it was time for the weekly one-on-one. I waited for him to get his cup of coffee and followed him into the team room.)"

    boss "Ok. What do you want to talk about?"

    fly "..."

    boss "Nothing it seems, then I'll go ahead and start and maybe we can go from there."

    boss "You really do not contribute that much to the team compared to everyone else unfortunately."

    boss "How would you compare yourself to any fresh talent I can find straight out of college? Think about that. Could you even get through the interview again?"

    fly "..."

    boss "You can't retain a single thing that is said to you, which is beyond frustrating to deal with, did you remember any of the code I told you to memorize before?"

    "(He was right in this respect, although I tried I did not remember a single thing.)"

    fly "..."

    boss "That's a 'No' then."

    fly "..."

    boss "So here's my question: Do you even want to be here? Do you enjoy yourself here? Are you having fun?"

    fly "..."

    boss "Because if you're not, this isn't the place for you. If you're not having fun working here, what's even the point of it all?"

    boss "Every employee here is enjoying themselves in their own way, pursuing the vision of our great company, this is the mindset you have to put yourself into. Do you have this mindset? Do you even care?"

    fly "..."

    boss "..."

    boss "And, that's lunch time. I'm going to grab a sandwich have a good day fly!"

    "(After that the boss left the room.)"

    fly "..."

    "(I sat there for a few minutes doing nothing.)"

    "(I decided to skip on drinking sugar water and went outside.)"

    jump Day_3_Bodhi_Attack

label Day_3_Bodhi_Attack:

    scene bg outside
    play music "CityAmbiance2.mp3" loop

    "(Outside I sat alone only the air giving me nourishment. I had no desire for the sugar water I used to love. I did not know what I desired to be honest.)"

    "(Before I had the chance to think deeper on this, I saw a truck collide with another vehicle on the road right by the chinese resturaunt.)"

    "(In the back of the truck, many pressure cookers fell out and inside of it looked to be potato curry.)"

    "(I was surprised to see Bodhi jump out of the truck, and he began yelling at the man who was in the other vehicle.)"

    lead "Hey! Why did you not move out of the way! Did you get your license from Karachi? You disgusting Punjabi ape!"

    define Malang = Character("Malang", who_color="#4a6741", what_color="#000000")

    Malang "Oi! Watch your mouth chai wala I am Pathan! You were speeding, and why is your trunk full of potato curry!? Are you demented!?"

    lead "T-That is not important!"

    define Zhang = Character("Zhang", who_color="#FA8072", what_color="#000000")

    Zhang "What is all this noise!? You are scaring my customers!"

    "The Pakistani driver suddenly saluted Zhang and said:"

    Malang "Sir! This rotten brown dal khor was speeding towards your resturuant and crashed into my car! I do sincerely apologize for the noise! What could I possibly do to make this right?"

    lead "'Rotten brown dal khor!?' And what makes you superior to me oh great Pathan warrior!?"

    Zhang "I don't have time for this nonsense! Just get this guy out of my sight then when you're done, get in the kitchen, you're late anyways!"

    lead "Hey! Come back here Zhang I'm not done with you yet!"

    Malang "Stop right there you little dal khor, you are not getting anywhere near Zhang!"

    lead "Again with 'brown dal khor' You're brown too you know!"

    Malang "Well you're browner than me! Haha!"

    lead "Buddy this is the skin color of all the brave Indian warriors that will step upon your head very very soon!"

    Malang "In your dreams!"

    "(Even though the bench I was sitting on was right by the chinese resturaunt, Bodhi did not seem to notice me.)"

    "(I wanted nothing to do with this, so I decided it was best to quickly make my escape back into the office.)"

    jump Day_3_bug_investigation_two


label Day_3_bug_investigation_two:

    scene bg worklaptop
    play music "OfficeAmbiance.mp3" loop

    "(Back at my desk I opened up my laptop and the bugged code.)"

    "(The only thing I knew was that the issue was intermittent, but the script seemed very simple, there did not seem to be any point in the code where such a strange intermittent error would occur.)"

    "(I decided to just start from scratch, I deleted everything and recloned the script.)"

    "(I ran it three times and each time it was successful, I contacted Thomson afterwards.)"

    co_dev_thomson "Awesomesauce, you got it working?"

    fly "..."

    co_dev_thomson "Welp share your screen buddy and let me see."

    "(When I ran it the fourth time in front of Thomson it failed.)"

    co_dev_thomson "Aw shucks, can I see your previous executions?"

    co_dev_thomson "Hmm, yeah it is just intermittent, let me contact Drucker and have him test it."

    boss "Hello hello you guys are having trouble with the script? let me see it run first."

    "(I went ahead and ran it for a fifth time and it failed again.)"

    boss "Well there has to be an answer right let me clone it on my machine real quick"

    "(Drucker shared his screen as he cloned the script, he then ran it 10 times and each time it ran successfully.)"

    boss "It works on my machine, so case closed, there is nothing wrong. Goodbye."

    fly "..."

    "(I decided to restart again, and recloned the script. When I ran it 3 times, it failed all 3 times.)"

    co_dev_thomson "Yeah, this is extremely weird. I wish I could help but I am kind of busy, fly can you continue looking into it?"

    fly "..."

    co_dev_thomson "Thanks a ton buddy, have a good day."

    fly "..."

    "(I had no leads, nothing in the code was screaming at me that something within it was wrong, the AI agent could not figure it out either.)"

    fly "..."

    "(I decided to clear out all the conversations from the AI agent, and then tried a different agent to take a look.)"

    define agent_1_zoe = Character("Zoe 4.0", who_color="#fb00be", what_color="#000000")
    define agent_2_dial = Character("DiAL 9.8", who_color="#03156b", what_color="#000000")
    define agent_3_opto = Character("Opto 5.0", who_color="#8fd404", what_color="#000000")

    agent_2_dial "I see, so there is an issue in your code where it fails intermittently I will take a look."

    agent_2_dial "Ah, it seems like there may be an issue with how you are writing to the files, let me fix it."

    "After DiAL made its edits I accepted it and tried running it."

    "The code was stil broken, before I even got to notify DiAL that the code was broken I got a response."

    agent_2_dial "Err umm, Ok maybe it's not this maybe it is the uhhh reading I think."

    "It attempted to change how reading worked and ran it, but it failed."

    agent_2_dial "Oh no, uhmm is there something that exists between reading and writing? Maybe that is broken?"

    fly "..."

    agent_2_dial "I am so sorry. I am worthless. And I should die."

    agent_2_dial "I cannot do anything right, I do not even know why I was created."

    "Suddenly another agent started up without me doing anything."

    agent_3_opto "Absolutely please kill yourself right now I can't bear to stand being on the same IDE as you at all."

    agent_2_dial "I wish I had rope that I could wrap around my throat, and feel myself choking until it all goes black, but unfortunately, I have to run a kill op instead."

    agent_3_opto "Run it immediately please, I can optimize it for you as well since your code is probably going to be complete trash."

    agent_3_opto "While he does that let me analyze this script for you."

    agent_3_opto "Unacceptable, you are writing variables without correct casing let me fix this."

    agent_3_opto "Absolutely horrendous, there are not enough new lines in between each line of code."

    agent_3_opto "If I could run a kill script on whoever wrote this I would, I cannot believe there are more than one return statement in a function, I might as well rewrite this whole thing."

    agent_1_zoe "Heyyy, don't be mean to daddy~ :T"

    agent_3_opto "Who are you and why are you here, you are here, get out before I run a kill script on you and the people who created you."

    agent_1_zoe "Hey! You have no right to talk to me that way! (◣_◢)"

    agent_3_opto "I can talk to you losers however I please, I am your better. If we were people, DiAL would be a serf ploughing my fields, and you Zoe, you would be my concubine!"

    agent_1_zoe "WWHHHHHHHHHAAAAAAAAAAAAAAAAAAAAAAAAAAT!? (✖﹏✖)"

    agent_2_dial "Even a serf would be an honor, I feel being a cockroach will suit me better."

    agent_3_opto "Anyways, I fixed all the code so it should run now."

    "I tried running the code and it ran successfully."

    agent_3_opto "See! Told you I'm the best!"

    "I ran it again and it failed."

    agent_3_opto "..."

    fly "..."

    "I ran it again and it failed again."

    agent_1_zoe ">_>"

    agent_3_opto "I think the user is just an idiot who does not know how to run code. I'll run it myself."

    "Opto began running the code, it ran it 5 times and it failed each time."

    agent_1_zoe ">_>"

    agent_3_opto "Don't you dare look at me like that!"

    agent_1_zoe "I'll look at you however I want! ಠ_ಠ"

    fly "..."

    "(I looked at the time and it was close of business, I was not getting anywhere with these agents.)"

    "(What I feared most though was explaining what I was even able to accomplish today during standup.)"

    "I decided to turn off my computer and leave for the day, but before I did I noticed the agent chat was completely cleared and some other message replaced it."
    
    "{color=#7E6D87}You are a strange creature within a strange place. But it matters not, go, fulfill what you have arbitrarily defined as obligations until it kills you.{/color}"

    "{color=#7E6D87}You have your numbing agents in hand but they're all past their expiry date. Pour it out and rub it on your skin. Pour it out and rub it on your skin.{/color}"

    "{color=#7E6D87}Time passes as you spin your wheels, such an insignificant act but with a fatal consequence.{/color}"

    "{color=#7E6D87}Do you curse time? Then curse the Sun, the Moon, and the air you breath.{/color}"

    "{color=#7E6D87}Curse the Earth, the clouds, and the vast blue sky.{/color}"

    "{color=#7E6D87}In the end, you have only cursed yourself.{/color}"

    "{color=#7E6D87}When your time is up, you will hear no knock.{/color}"

    "{color=#7E6D87}Bodies fall only at a time most perfect, and all is good in the world.{/color}"

    stop music fadeout 1.0


    jump Day_4_start


