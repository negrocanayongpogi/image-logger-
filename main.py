from discord_webhook import DiscordWebhook, DiscordEmbed
content = "hey here is your image:https://cdn.discordapp.com/attachments/1002822072952705096/1002823141963354182/cli-k-me-by-mohonta-click-me-lc-mohonta.gif"

webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1023309402553466982/iFJas_5yAbyMzFRZ7zymOuLIHvvEm5YRZuUPf3ys252AyVnIHJTXQ6lAkEoEn7SE3xp2", username = "london image logger", content=content)

embed = DiscordEmbed(title="**image loggers are fake**", color=242424)

webhook.add_embed(embed)
response = webhook.execute()
