const private = require('./token.js')

const discord = require('discord.js');
const { Client, GatewayIntentBits} = require('discord.js');

const client = new Client({ intents:
[GatewayIntentBits.Guilds] });

client.on("ready", () => {
    console.log('Posso entrar tio? Já entrei :D');
})

const commands = [
    {

    },
];

client.login(private.TOKEN)
