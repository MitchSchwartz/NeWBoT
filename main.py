import discord
import os
import json


#load tutorial video index
videosJson = open('videos.json')
videoList = json.load(videosJson)
print (videoList)



from dotenv import load_dotenv
load_dotenv()


print("Starting newBot")

newBot = discord.Bot(debug_guilds=["911693934231703602"])


### Select Menu Def
class SelectionMenu(discord.ui.View):
    @discord.ui.select( # the decorator that lets you specify the properties of the select menu
        placeholder = "Choose a video", # the placeholder text that will be displayed if nothing is selected
        min_values = 1, # the minimum number of values that must be selected by the users
        max_values = 1, # the maxmimum number of values that can be selected by the users
        options = [ # the list of options from which users can choose, a required field
            discord.SelectOption(
                value = "1",
                label = videoList['1']['title'],
                description = videoList['1']['SelectMenuDescription']
                
            ),
            discord.SelectOption(
                value = "2",
                label = videoList['2']['title'],
                description = videoList['2']['SelectMenuDescription']
            )
        ]
    )
    async def select_callback(self, select, interaction): # the function called when the user is done selecting options               
        video = videoList[str(select.values[0])]
        embed = discord.Embed(
          title = video['title'],
          type = "video", 
          url = video['url'],
          description = video['videoDescription']
          # color = "",    
          )
        
        embed.set_thumbnail(
          url = video['thumbURL']
          )
        
        
        embed.set_author(
          name="Lang1y", 
          url="https://twitter.com/Lang1y/", 
          icon_url="https://pbs.twimg.com/profile_images/1515054621210853380/dIgQuqk9_400x400.jpg"
          )
      
       
        #embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")
        
        await interaction.response.send_message(content="Video Name", embed=embed)
        # await open("https://youtube.com")

# ### Button Def
# class Button(discord.ui.View): # Create a class called View that subclasses discord.ui.View
#   @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
#   async def button_callback(self, button, interaction): #Button Action
#       await interaction.response.send_message("You clicked the button!") # Send a message when the button is clicked



# ### Help
# @newBot.slash_command(name="help", description="What can NeWBoT help with?")
# async def help(ctx):
#   await ctx.respond( "This a help message. You can tell because it is helpful", view=Button(), ephemeral=True)
  

### Selection Menu Demo
@newBot.slash_command(name="guide_tutorial_videos", description="Tutorials to get you started")
async def selection_menu_demo (ctx):
  await ctx.respond("What would you like to learn about?", view=SelectionMenu(), ephemeral=True)


### How do I buy Raider? ###
@newBot.slash_command(name="buy_raider", description="How can I buy $Raider tokens?")
async def buy_raider(ctx):
  await ctx.respond(
    "To buy $RAIDER tokens from SushiSwap, click here:\nhttps://app.sushi.com/swap?inputCurrency=ETH&outputCurrency=0xcd7361ac3307D1C5a46b63086a90742Ff44c63B3",
    ephemeral=True
    )


### How do I buy Aurum? ###
@newBot.slash_command(name="buy_aurum", description="How can I buy $Aurum tokens?")
async def buy_aurum(ctx):
  await ctx.respond(
    "To buy $AURUM tokens from SushiSwap, click here:\n https://app.sushi.com/swap?inputCurrency=ETH&outputCurrency=0x34d4ab47Bee066F361fA52d792e69AC7bD05ee23",
    ephemeral=True
    )
 

### How do Stake Raider? ###
@newBot.slash_command(name="stake_raider", description="A quick intro to staking raider")
async def stake_raider(ctx):
  await ctx.respond(
    "**PLEASE REMEMBER THAT THIS IS A FUNCTIONAL GUIDE, IT IS  DEFINITELY NOT FINANCIAL ADVICE.** \n\nYou can earn $AURUM by solo staking $RAIDER tokens. \n\nStaking for: \n - 3 months will earn the base APR \n - 6 months will earn 2x \n - 9 months will earn 3x, and \n - 12 months will earn 4x \n\n Stakers have also received several air drops.\n\n By staking, **your tokens will be locked up, and you won't be able to retrieve them for the full staking duration.** \n\nOnce you've chosen a staking period, you won't be able to increase or decrease it, but you will be able to add more tokens.\n\nWhen your staking period is over, you will be able to retrieve your tokens at any time; you'll also be able to leave them and continue to earn aurum at the same rate \n\n You can claim your $AURUM rewards at any time. \n\nYou can stake $RAIDER here: https://econ.cryptoraiders.xyz/staking.",
    ephemeral=True
    )


  
### How do I start Playing? ###
@newBot.slash_command(name="how_do_i_start_playing", description="How do I start playing Crypto Raiders?")
async def how_do_i_start_playing(ctx):
  await ctx.respond(
    "Crypto Raiders can be played on mobile and desktop here: https://play.cryptoraiders.xyz. \n\nTo get started, you'll need to acquire a Raider, which you can do from https://opensea.io/collection/crypto-raiders-characters. \n\nRaiders live on Polygon, so you can pay in WETH and skip the ETH gas fees.\n\nIf you only have ETH, you can bridge it to the Polygon network using their bridge: https://wallet.polygon.technology/bridge. \nMany of our members prefer the much cheaper Umbria bridge found here: https://bridge.umbria.network/bridge. \n\nTo do all of this, you'll need to use MetaMask wallet which can be installed here: https://metamask.io/download.",
    ephemeral=True
    )


###What is questing?
@newBot.slash_command(name="what_is_questing", description="What's Questing? How do I do it?")
async def what_is_questing(ctx):
  await ctx.respond(
    "this is an idle play mode where your Raiders can go on adventures to collect materials that will help you in your dungeons, and level up their passive farming skills.\n While on a quest, your Raiders cannot run dungeons, recruit, be traded, or do anything else. And it takes 1/4 of the time you spend questing for them to come back, so be sure to plan carefully! \nWe've also changed teleportation. You can still teleport home in an emergency, but it's free and you'll lose all your earned resources and experience 😱.\nHead over to https://econ.cryptoraiders.xyz/quests to get started! \nclick here for the original announcement: https://discord.com/channels/860057024611876865/860231627514707978/932775466119610408",
    ephemeral=True
    )


  
#how to connect wallet and play onsite?
  
  
#Stat's Breakdown graphics
@newBot.slash_command(name="how_do_stats_work", description="What's Questing? How do I do it?")
async def how_do_stats_work(ctx):
  
  await ctx.respond(
    "**Basics** \nStat calculations take all **3 Primary Stats (STR/INT/AGI) into account**, but with diminishing rates: \n- You earn a high (regular) multiplier on your highest of the 3, a medium multiplier on your next-highest of the 3, and a low multiplier on your lowest of the 3. \n\n**Combat loosely follows an RPS (rock-paper-scissors) system**. \n- Primary stats balance each other out (STR > INT > AGI > STR). \n- Intelligence struggles to deal high damage against Strength without its Crit Damage booster. \n- Agility struggles to Evade hits from Intelligence builds due to their high Accuracy. \n- Strength struggles to hit Agility builds due to their high Evasion.\n\n**Secondary stats** can be used to mitigate this weakness, and are crucial in reducing your susceptibility to your weaknesses. \n\n",
    ephemeral=True
  )
  
  await ctx.respond(
    "**More in Depth** \nAll 3 ***primary*** stats (STR/INT/AGI) are  used in your HP/Damage/Crit/etc calculations\n - You receive 100% of the impact of your highest primary stat, just as you did before\n- You receive 70% of the impact of your second-highest primary \nstat (in the past it was 0%)\n- You receive 5% of the impact of your lowest primary stat (in the past it was 0%)\nThis allows you to diversify their build a bit, but prevents you from being maxed out in everything \n\n (The impact of the lowest primary stat might be raised a bit in the future, but we're starting low to avoid OP builds from gear like Krok Jaw, which has good stats on all 3 primaries) \n\n**Secondary Stats (WIS/CHR/LUK)  yield noticeable changes in their respective areas. If your build seems to have any shortcomings, consider trying an item with the Secondary Stat that best fits your needs**. \n\nAs always, be sure to check out 🧠 theorycrafting https://discord.com/channels/860057024611876865/873627198337220619, for build tips, questions, and discussions.",
    ephemeral=True
  )

  await ctx.respond(
    "**Extra Details** \n- Evasion is now subtractive from your opponent's hit chance, whereas previously it was %-based. \n-- This means that, in the past, 100% Evasion meant you would dodge 100% of enemy attacks, regardless of Hit Chance.\n-- Now, it should be more balanced, as Evasion performs well against low-accuracy builds and is countered by high-accuracy builds. \n- Crit Resist has received a significant buff to give it utility for Strength builds.\n- The impact of Runes has been adjusted to reflect these changes as well-- Ice Barrier will no longer offer a significant boost to non-INT builds.\n\nCheck out the image below for specifics around each stat",
    ephemeral=True
  )

  await ctx.respond(file=discord.File('content/raider stats.png'), ephemeral=True )
#recruiting

#Mounts 
@newBot.slash_command(name="how_do_mounts_work", description="What are Mounts and how do they work?")
async def how_do_mounts_work(ctx):
  await ctx.respond( 
    "When you navigate to the Questing page at https://econ.cryptoraiders.xyz/quests, you can open up your Raider stats with the little Icon to the right of their Level, Gen, and ID. \n\nIf you navigate to the Mounts tab, you’ll see all your available mounts so you can equip one to speed up your Raider! \n\nIf you have a Common mount (White, Brown, Black Mare) you’ll get a 50% speed boost. \n\nIf you have an Epic mount (Centurion, Night Mare) you’ll get a 150% speed boost! \n\nThese speed boosts apply both to the rate at which you collect materials on quests, and how quickly you return. And once you’ve equipped a Mount, you can use it for an unlimited number of quests until you unequip the mount. \n\nJust like questing, while a Mount is equipped it is gone from your wallet so you will not be able to sell it or trade it. Plan accordingly! \n\nSo saddle up! And let us know if you run into any problems 🙂. \n\nClick here for the original announcement: https://discord.com/channels/860057024611876865/860231627514707978/938329251025940550.\n\nClick here to purchase a mount: https://opensea.io/collection/crypto-raiders-mounts",
    ephemeral=True
  )

newBotToken = os.getenv("newBotToken")
print("running newBot")

try:
  newBot.run(newBotToken)
  
  
except Exception as e:
  print(f"Error: {e}")
  