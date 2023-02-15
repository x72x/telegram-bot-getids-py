# pyGetIDSBot

> ## ⚠️ Status of this project
>
> The original developers of this bot mostly moved on and away from Telegram bot development. Please consider this code and bot unmaintained. It may still work, but we won't rush to fix things anymore.

## Introduction

pyGetIDSBot is a chatbot for the Telegram Messaging Plattform which main purpose
is to extract useful informations from messages that are normally hidden and
to enhance them. This means...

## Using this bot

**Option A:** Use the version we host at https://t.me/pyGetIDSBot

**Option B:** Host one yourself. You will need a bot token from the
[BotFather](https://t.me/botfather) .

## Account creation dates

Most people want to use this, so here is a bit of explanation for all of you:
Telegram gives each chat (that is users, bots, groups and channels) a globally
unique numerical id. These id numbers aren't given out sequentially, so two users
signing up at the exact same time will probably have a difference of up to a few
millions. Two possible reasons are:

- Sharding: Telegram registrations won't all happen on the same server. To avoid
  giving out the same id twice, all registration servers reserve a range of ids
  from the central registry and periodically fetch new ones.
- Obfuscation: You should not be able to guess the signup date from one's id.

This is still speculation, and we don't know for certain, but averaged out over
a year or so, the IDs do still increase. There are some exceptions, but guessing
is still possible.

We collected a bunch of ids for which we knew the rough creation dates, anonymized
the dates and used some dark magic called "maths" to estimate a creation date.

## License and Copyright

MIT for this project, some BSD and Apache License, Version 2.0 for it's dependencies.
Copyright 2021 Jonas Zohren & other contributors.
