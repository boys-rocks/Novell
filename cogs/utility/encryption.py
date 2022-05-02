import base64
import binascii
import codecs
import hashlib
import secrets
import discord
from discord.ext import commands
from utils.format import *


class Encryption(commands.Cog):
    """this cog contains all the encryption/decryption commands"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.group(aliases=['encrypt'])
    async def encode(self, ctx):
        """ All encode methods """
        if ctx.invoked_subcommand is None:
            eb=discord.Embed(colour=discord.Colour.random())
            eb.description="""\
**This is a Group Command!!**
**Usage:**
```
Lf!Encode [TYPE] [TO ENCODE]
```
**Types:**
```fix
0. TYPE    | ALIAS
1. Base64  | b64
2. Base32  | b32
3. Base85  | b85
4. Ascii85 | a85
5. Rot13   | r13
6. Hex Code| hex
7. Morse   | mrs
8. MD5     | md5
9. SHA256  | s512
10. SHA512 | s256
```
            """
            eb.timestamp=ctx.message.created_at
            eb.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar_url)
            await ctx.send(embed=eb)

    @commands.group(aliases=['decrypt'])
    async def decode(self, ctx):
        """ All decode methods """
        if ctx.invoked_subcommand is None:
            eb=discord.Embed(colour=discord.Colour.random())
            eb.description="""\
**This is a Group Command!!**
**Usage:**
```
Lf!Decode [TYPE] [TO DECODE]
```
**Types:**
```fix
0. TYPE    | ALIAS
1. Base64  | b64
2. Base32  | b32
3. Base85  | b85
4. Ascii85 | a85
5. Rot13   | r13
6. Hex Code| hex
7. Morse   | mrs
```
            """
            eb.timestamp=ctx.message.created_at
            eb.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar_url)
            await ctx.send(embed=eb)

    async def encryptout(self, ctx, convert, txtinput):
        '''
        

        Args:
            ctx ([type]): [description]
            convert ([type]): [description]
            txtinput ([type]): [description]

        Returns:
            [type]: [description]
        '''
        if len(txtinput) > 1900:
            return await ctx.send(embed=discord.Embed(
                description=f"**The result was too long (more than 1900 letters), sorry {ctx.author.name}**"
            ))

        try:
            await ctx.send(embed=discord.Embed(description=f"📑**{convert}**\n```fix\n{txtinput.decode('UTF-8')}```"))
        except AttributeError:
            await ctx.send(embed=discord.Embed(description=f"📑**{convert}**\n```fix\n{txtinput}```"))

    @encode.command(name="base32", aliases=["b32"])
    async def encode_base32(self, ctx, *, txtinput: commands.clean_content):
        """ Encode in base32 """
        await self.encryptout(
            ctx, "Text -> Base32", base64.b32encode(txtinput.encode("UTF-8"))
        )

    @decode.command(name="base32", aliases=["b32"])
    async def decode_base32(self, ctx, *, txtinput: str):
        """ Decode in base32 """
        try:
            await self.encryptout(
                ctx, "Base32 -> Text", base64.b32decode(txtinput.encode("UTF-8"))
            )
        except Exception:
            await ctx.send("Invalid base32...",delete_after=7)

    @encode.command(name="base64", aliases=["b64"])
    async def encode_base64(self, ctx, *, txtinput: commands.clean_content):
        """ Encode in base64 """
        await self.encryptout(
            ctx, "Text -> Base64", base64.urlsafe_b64encode(txtinput.encode("UTF-8"))
        )

    @decode.command(name="base64", aliases=["b64"])
    async def decode_base64(self, ctx, *, txtinput: str):
        """ Decode in base64 """
        try:
            await self.encryptout(
                ctx,
                "Base64 -> Text",
                base64.urlsafe_b64decode(txtinput.encode("UTF-8")),
            )
        except Exception:
            await ctx.send("Invalid base64...",delete_after=7)

    @encode.command(name="rot13", aliases=["r13"])
    async def encode_rot13(self, ctx, *, txtinput: commands.clean_content):
        """ Encode in rot13 """
        await self.encryptout(ctx, "Text -> rot13", codecs.decode(txtinput, "rot_13"))

    @decode.command(name="rot13", aliases=["r13"])
    async def decode_rot13(self, ctx, *, txtinput: str):
        """ Decode in rot13 """
        try:
            await self.encryptout(
                ctx, "Rot13 -> Text", codecs.decode(txtinput, "rot_13")
            )
        except Exception:
            await ctx.send("Invalid rot13...",delete_after=7)

    @encode.command(name="hex")
    async def encode_hex(self, ctx, *, txtinput: commands.clean_content):
        """ Encode in hex """
        await self.encryptout(
            ctx, "Text -> Hex Code", binascii.hexlify(txtinput.encode("UTF-8"))
        )

    @decode.command(name="hex")
    async def decode_hex(self, ctx, *, txtinput: str):
        """ Decode in hex """
        try:
            await self.encryptout(
                ctx, "Hex Code -> Text", binascii.unhexlify(txtinput.encode("UTF-8"))
            )
        except Exception:
            await ctx.send("Invalid hex...",delete_after=7)

    @encode.command(name="base85", aliases=["b85"])
    async def encode_base85(self, ctx, *, txtinput: commands.clean_content):
        """ Encode in base85 """
        await self.encryptout(
            ctx, "Text -> Base85", base64.b85encode(txtinput.encode("UTF-8"))
        )

    @decode.command(name="base85", aliases=["b85"])
    async def decode_base85(self, ctx, *, txtinput: str):
        """ Decode in base85 """
        try:
            await self.encryptout(
                ctx, "Base85 -> Text", base64.b85decode(txtinput.encode("UTF-8"))
            )
        except Exception:
            await ctx.send("Invalid base85...",delete_after=7)

    @encode.command(name="ascii85", aliases=["a85"])
    async def encode_ascii85(self, ctx, *, txtinput: commands.clean_content):
        """ Encode in ASCII85 """
        await self.encryptout(
            ctx, "Text -> ASCII85", base64.a85encode(txtinput.encode("UTF-8"))
        )

    @decode.command(name="ascii85", aliases=["a85"])
    async def decode_ascii85(self, ctx, *, txtinput: str):
        """ Decode in ASCII85 """
        try:
            await self.encryptout(
                ctx, "ASCII85 -> Text", base64.a85decode(txtinput.encode("UTF-8"))
            )
        except Exception:
            await ctx.send("Invalid ASCII85...",delete_after=7)

            
    @encode.command(name="morse",aliases=['mrs'])
    async def encode_morse(self,ctx,*,txtinput:str):
        """Encode in Morse codes"""
        await self.encryptout(ctx,"Text -> Morse Code",morse("encode",str(txtinput)))
    
    @decode.command(name="morse",aliases=['mrs'])
    async def decode_morse(self,ctx,*,txtinput:str):
        """Decode Morse codes"""
        await self.encryptout(ctx,"Morse Code -> Text",morse("decode",str(txtinput)))
        
    @encode.command(name="md5")
    async def encode_md5(self,ctx,*,txtinput:str):
        """Encode to MD5 sums"""
        await self.encryptout(ctx,"Text -> MD5 hash",hashlib.md5(bytes(txtinput.encode("utf-8"))).hexdigest())
    
    @encode.command(name="sha256",alises=['s256'])
    async def encode_sha256(self,ctx,*,txtinput:str):
        """Encode toSHA256"""
        await self.encryptout(ctx,"Text -> SHA256 hash",hashlib.sha256(bytes(txtinput.encode("utf-8"))).hexdigest())
        
    @encode.command(name="sha512",alises=['s512'])
    async def encode_sha512(self,ctx,*,txtinput:str):
        """Encode toSHA512"""
        await self.encryptout(ctx,"Text -> SHA512 hash",hashlib.sha512(bytes(txtinput.encode("utf-8"))).hexdigest())
        
        
    @decode.command(name="hash",aliases=['md5','sha256','sha512','s512','s256'])
    async def hashes(self,ctx):
        eb=discord.Embed(title=f"Nah!!",colour=discord.Colour.random())
        eb.description=f"""\
        {str(ctx.invoked_with).upper()} is a [cryptographic (one-way) hash functionality](http://en.wikipedia.org/wiki/Cryptographic_hash_function), so there is no direct way to decode it.
        The entire purpose of a cryptographic hash functionality is that you **can't UNDO it.*
        One thing you can do is a [brute-force strategy](http://en.wikipedia.org/wiki/Password_cracking), where you guess what was hashed, then hash it with the same function and see if it matches. Unless the hashed data is very easy to guess, it could take a long time though.
        > You may find the question "[Difference between hashing a password and encrypting it](https://stackoverflow.com/questions/326699/difference-between-hashing-a-password-and-encrypting-it)" interesting....suggesting you to read it...
        """
        eb.timestamp=ctx.message.created_at
        eb.set_footer(text=f"{ctx.author.name} tryna become \"Smarty Pants\"!!",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=eb)
        

def setup(bot):
    bot.add_cog(Encryption(bot))
