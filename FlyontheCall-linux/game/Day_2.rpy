init:
    image bg worklaptop = "worklaptop.jpg"
    image bg blackscreen = "blackscreen.jpg"
    image bg ceilinglight = "ceilinglight.jpg"

label Day_2_Start:

    scene bg blackscreen
    play music "OfficeAmbiance2.mp3" loop

    boss "Alright good morning and gooooooood day! If I am not wrong I believe we have a release scheduled for next week Monday am I correct?"

    co_dev_jai "Yes Drucker that is the plan."

    boss "Very good, please do a write up on the implementation plan, the backout plan, the shakeout plan, write up the testing document, the NFR document and the P2P document."

    boss "Then do a SAST scan, SCA scan, DAST scan, MRI Scan, CT Scan. Once you are done with that begin the Cystoscopy operation and then, ah damn, it's gonna cut into lunch but at 11:30AM we have to the C-Section."

    boss "After that we gotta mix the batter, but do not overmix but also do not undermix, make sure it is a little clumpy, Goooot it?"

    co_dev_jai "Yes Drucker, it will be done."

    boss "Goooooood! and be sure to update the ticket as you go. Although, I just remembered, weren't you and Thomson supposed to have demo yesterday? What happened to that?"

    co_dev_jai "Sorry about that Drucker, GO Team contacted me and an intern accidently deleted an image so their app was down, I had to assist and that took up the day."

    co_dev_jai "But everything is good on their end now, and the intern was dismissed."

    boss "That is unfortunate, but not our problem thankfully, Thank you fly for bringing this up yesterday, and thank you Jai for updating me on this."

    boss "Now, Thomson! you said your work was done yesterday, but I see it is still 'IN DEV' on the board!"

    co_dev_thomson "Sorry, the item is pretty much done but-"

    boss "Nope, not adequate we went over this yesterday, I need forward answers, none of this wishy washy stuff now alright. Is it done?"

    co_dev_thomson "No."

    boss "Can you finish it today?"
    
    co_dev_thomson "Probably before lunch."

    boss "'Probably?'"

    co_dev_thomson "I can get it done before lunch."

    boss "Great! keep me posted."

    boss "Finally Fly, what updates do you have for us."

    lead "I have to take a look at the edits he had made, Once I am done reviewing those edits I'll write up his next task."

    boss "Great, thanks for that, and have a good day everyone."

    "(Right after standup Bodhi called me.)"

    lead "Good Morning Fly, I have some things I need your help with but one thing first."

    lead "Don't tell anyone, or ask anyone else for help on what I am going to assign to you."

    lead "I think it may lead to a lot of confusion if anyone else was involved with I want to assign you which cause the delivery of the item to be delayed."

    lead "As you know, it is unacceptable for anything we work on to be delivered later than the due date, it reflects badly on all of us."

    lead "I hope we understand each other, you will own this assignment and no one else will, are we clear?"

    fly "..."

    lead "Sounds good, I will call you in a few minutes regarding the details. I need a coffee break."

    fly "..."

    "(I was not sure what to do in the meantime.)"

    fly "..."
    
    "(Thirty minutes had passed and I did not get a response.)"

    "(I decided to go up to Jai to see if he needed help with anything.)"

    jump Day_2_Jai_Convo


label Day_2_Jai_Convo:

    scene bg ceilinglight

    co_dev_jai "There are some vulnerability reports that need to be checked on. It pains me to have someone else do the work, and I would rather do it myself."

    fly "..."

    co_dev_jai "If you insist, my companion, I will leave you to it, but do not hesitate to ask me for any help you need."

    "(When I checked the website there was six vulnerabilities that we were notified about a month ago, the deadline for acknowledging it and deploying a fix was 5PM today.)"

    fly "..."

    co_dev_jai "How horrifying, we must fix this post haste!"
    
    co_dev_jai "If we do not have this fixed by the deadline, I will exile myself into the mountains of Kyrgyzstan, where I will mine minerals for the rest of my life, I cannot think of a more fitting punishment for a failure this egregious."

    fly "..."

    "(I got to work on it immediately.)"

    "(I was able to submit the ticket to deal with the vulnerabilities, but I was blocked from making the change myself so I had to contact someone to do it for me, but it seems they were on vacation.)"

    fly "..."

    co_dev_jai "Fly, my companion, you chose the wrong template. Here, cancel this ticket and I'll guide you."
    
    co_dev_jai "You see, there is a list of templates that we use when submitting tickets, we give our thanks to the little helpers who create them."
    
    co_dev_jai "There are even templates used that are created specifically to bypass checks by the higher ups, I consider this very duplicitous, but, I won't raise any alarms if you chose to do it this way, as you are my companion."
    
    "(I did not have much time before deadline, so I decided to use one of the bypassing templates.)"
    
    "(After the ticket was submitted I began setting the start time and end time.)"

    "(I attempted to write that the end time had to be today at 5PM, but the system would revert my change to the current time. It would then notify me that the end date had to be after the start date and erase what I entered.)"

    "(This was peculiar design to say the least, as I was not submitting the ticket yet, I just wanted to fill in the time.)"

    "(This happened 5 times before I looked at Jai.)"

    co_dev_jai "This is very unfortunate, If I could use my two hands to fix this issue I would, but alas, I am not on the team that works on this system. My advice would be to copy the start time of the ticket on a notepad, edit it, then paste it into the end time."

    "(Once that was done I wrote all the details needed for the ticket, set up the payload file to deal with the vulnerabilities and ran the pipeline.)"

    jump DAY_2_Error


label DAY_2_Error:

    scene bg worklaptop

    "(Once that was done I wrote all the details needed for the ticket, set up the payload file to deal with the vulnerabilities and ran the pipeline.)"

    "(The pipeline ran for 10 minutes before failing.)"

    "(I read the error message which stated the following:)"

    "{color=#FF0000}ERROR: THE ONLY CEREAL I HAD LEFT WAS THE DISGUSTING TASTELESS OAT ONES AND THE MILK WAS EXPIRED. PLEASE RETRY.{/color}"

    "(I ran it again, which took 7 minutes.)"

    "{color=#FF0000}ERROR: I TWIPPED AND FELL AND IT HWUTS WEALLY BWAD T_T. PWEASE RETWY.{/color}"

    "(I ran it again, this time taking 12 minutes.)"

    "{color=#FF0000}ERROR: HELLO, WE ARE CALLING YOU ABOUT DOING A ROOF INSPECTION AT YOUR RESIDENCE IN LEANDER, PLEASE LET US KNOW YOUR AVAILABILITY. PLEASE RETRY.{/color}"

    fly "..."

    "(I began to wonder how something this broken ever reached widespread adoption in the industry.)"

    "(I ran it again, this time it took 9 minutes.)"

    "{color=#00ff00}SUCCESS: PAYLOAD DEPLOYED.{/color}"

    "(Finally, as I was about to leave for lunch but I noticed after the success message there was still information for me to look at if I scrolled down, out of curiosity I did.)"

    "{color=#7E6D87}Where are you?{/color}"

    "{color=#7E6D87}In an officespace within the big city, with a tie around your neck.{/color}"

    "{color=#7E6D87}What are you?{/color}"

    "{color=#7E6D87}A simple fly, who has betrayed his inclinations.{/color}"

    "{color=#7E6D87}How are you?{/color}"

    "{color=#7E6D87}Such an absurd question when rent is due.{/color}"

    fly "..."

    "(I closed my laptop and made sure to put extra sugar in my water for lunch.)"

    jump Day_2_boss_convo


label Day_2_boss_convo:

    scene bg blackscreen

    "(Once I finished lunch and got up from my chair I was startled by my boss, who was waiting right behind me. I was not sure how long he had been standing there, or for what reason.)"

    boss "Hello Fly, I hope you have something to work on during the afternoon."

    fly "..."

    boss "Waiting for Bodhi is not work, that is called dilly dallying I will assign you something right now: There is something quick that we can sneak into the release next week, there is an image update for Nergee, go on their page and it should have the latest version."

    boss "Let me know when you update it so I can approve the merge."

    jump Day_2_pasting_img

label Day_2_pasting_img:

    scene bg worklaptop

    "(Once I was done pasting the image I began doing a merge request.)"

    "(Once it began I noticed something rather peculiar, the scans was showing that every single test we have written failed.)"

    "(I tried running all of those tests locally and they were all running fine. I quickly notified Drucker and he came over to my desk.)"

    boss "Let me take a look, hmmmm."

    boss "Are you purposely committing sabotage or?"

    fly "..."

    boss "You broke the tests and which is why it is failing, Did you actually read through the tests?"

    fly "..."

    boss "Ok fly look at the tests thoroughly before stealing my attention from me, if it's broken fix it."

    "(Upon looking at the scans, the error did not seem to really make sense, it just pointed to the imports and said that it did not exist, but locally they did exist and the tests worked fine.)"
    
    "(The issue probably had to do with how these tests were being read.)"

    fly "..."

    "(I contacted the boss again attempting to explain the issue.)"

    boss "Ok, and how long has this been an issue?"
    
    fly "..."
    
    boss "You don't know. So, possibly our tests have been consistently failing and we have no reference on how long this possibly has been going on, for all I know you and the team have been ignoring it or not bothering to look into it, until now?"
    
    boss "Absolutely unacceptable, this very much has replaced the milk in my cereal with piss."
    
    boss "Whatever just stop what you're doing and I'll grab Jai to take a look at it."
    
    "(The boss left, and I was left with nothing to do.)"
    
    fly "..."

    "(Anxious to be caught not doing work, I went through our old documentation and updated anything that was outdated.)"

    "(After a couple of hours Drucker came back.)"

    boss "Everything is fine I just ignored the failed tests and approved the merge. See that was not so hard right? You really wasted my time with this."

    fly "..."
    
    boss "Although next time, we are going to have to get a better understanding on how this system works. I'll create a ticket for you to investigate this."

    boss "Also, what were you doing while I was gone?"

    "(I was about to show Drucker the changes I made to the outdated documentation, but he seemed to be completely ignoring what I was showing him.)"

    boss "Ah so you did nothing for four hours, fixing grammar on documentation does not qualify as work to me, sorry."

    fly "..."
    
    boss "This is really not a good look, while I was figuring out your issue for you, you were playing English teacher. Very bad kid, very bad."
    
    boss "Alright, well don't be the last one out of the office, see you tomorrow."

    "(His final statement was what made me realize that the work day had ended. I did not notice the time fly past me. And it would be safe to say I won't notice the speed at which it flows tomorrow, and the day after.)"

    "(Regardless, I worked for an extra hour on various tasks that were neglected and would be neglected if I did not work on them now.)"

    fly "..."

    "(Bodhi never did call me back like he said he would.)"
    
    stop music fadeout 1.0

    jump Day_3_start
