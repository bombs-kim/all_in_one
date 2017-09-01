__all__ = ['storefarm_common_all_trans']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['b64pad', 'bnpDivRemTo', 'bnpDRShiftTo', 'intAt', 'RSADoPublic', 'get_encpw', 'montConvert', 'RSAEncrypt', 'montRevert', 'hex2b64', 'parseBigInt', 'nbv', 'am2', 'bnpInvDigit', 'bnpRShiftTo', 'rr', 'rng_get_bytes', 'b64tohex', 'int2char', 'nbits', 'cConvert', 'rng_get_byte', 'linebrk', 'pkcs1pad2', 'SecureRandom', 'bnAbs', 'bnpIsEven', 'bnMod', 'bnpFromInt', 'bnpMultiplyTo', 'vv', 'bnToString', 'b64map', 'bnModPowInt', 'bnpFromString', 'BigInteger', 'prng_newstate', 'j_lm', 'cReduce', 'ARC4next', 'montReduce', 'RSAKey', 'bnpCopyTo', 'bnpSquareTo', 'byte2Hex', 'cRevert', 'bnpDLShiftTo', 'bnBitLength', 'bnpLShiftTo', 'BI_RM', 'ARC4init', 'bnpExp', 'rng_seed_time', 'montSqrTo', 'montMulTo', '$', 'bnNegate', 'rng_seed_int', 'bnCompareTo', 'cSqrTo', 'BI_RC', 'bnpClamp', 'clearErrorLayers', 'am1', 'keySplit', 'bnpSubTo', 'cMulTo', 'Montgomery', 'canary', 'BI_FP', 'nbi', 'RSASetPublic', 'Classic', 'am3', 'Arcfour', 'getLenChar', 'b64toBA'])
@Js
def PyJsHoisted_bnpDivRemTo_(a, b, c, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'c':c, 'b':b}, var)
    var.registers(['d', 'b', 'f', 'e', 'j', 'a', 'o', 'n', 'l', 'p', 'r', 's', 'c', 'i', 'k', 'h', 'm', 'q', 'g'])
    var.put('d', var.get('a').callprop('abs'))
    if (var.get('d').get('t')<=Js(0.0)):
        return var.get('undefined')
    var.put('e', var.get(u"this").callprop('abs'))
    if (var.get('e').get('t')<var.get('d').get('t')):
        if (var.get('b')!=var.get(u"null")):
            var.get('b').callprop('fromInt', Js(0.0))
        if (var.get('c')!=var.get(u"null")):
            var.get(u"this").callprop('copyTo', var.get('c'))
        return var.get('undefined')
    if (var.get('c')==var.get(u"null")):
        var.put('c', var.get('nbi')())
    var.put('f', var.get('nbi')())
    var.put('g', var.get(u"this").get('s'))
    var.put('h', var.get('a').get('s'))
    var.put('i', (var.get(u"this").get('DB')-var.get('nbits')(var.get('d').get((var.get('d').get('t')-Js(1.0))))))
    if (var.get('i')>Js(0.0)):
        var.get('d').callprop('lShiftTo', var.get('i'), var.get('f'))
        var.get('e').callprop('lShiftTo', var.get('i'), var.get('c'))
    else:
        var.get('d').callprop('copyTo', var.get('f'))
        var.get('e').callprop('copyTo', var.get('c'))
    var.put('j', var.get('f').get('t'))
    var.put('k', var.get('f').get((var.get('j')-Js(1.0))))
    if (var.get('k')==Js(0.0)):
        return var.get('undefined')
    var.put('l', ((var.get('k')*(Js(1.0)<<var.get(u"this").get('F1')))+((var.get('f').get((var.get('j')-Js(2.0)))>>var.get(u"this").get('F2')) if (var.get('j')>Js(1.0)) else Js(0.0))))
    var.put('m', (var.get(u"this").get('FV')/var.get('l')))
    var.put('n', ((Js(1.0)<<var.get(u"this").get('F1'))/var.get('l')))
    var.put('o', (Js(1.0)<<var.get(u"this").get('F2')))
    var.put('p', var.get('c').get('t'))
    var.put('q', (var.get('p')-var.get('j')))
    var.put('r', (var.get('nbi')() if (var.get('b')==var.get(u"null")) else var.get('b')))
    var.get('f').callprop('dlShiftTo', var.get('q'), var.get('r'))
    if (var.get('c').callprop('compareTo', var.get('r'))>=Js(0.0)):
        var.get('c').put((var.get('c').put('t',Js(var.get('c').get('t').to_number())+Js(1))-Js(1)), Js(1.0))
        var.get('c').callprop('subTo', var.get('r'), var.get('c'))
    var.get('BigInteger').get('ONE').callprop('dlShiftTo', var.get('j'), var.get('r'))
    var.get('r').callprop('subTo', var.get('f'), var.get('f'))
    while (var.get('f').get('t')<var.get('j')):
        var.get('f').put((var.get('f').put('t',Js(var.get('f').get('t').to_number())+Js(1))-Js(1)), Js(0.0))
    while (var.put('q',Js(var.get('q').to_number())-Js(1))>=Js(0.0)):
        var.put('s', (var.get(u"this").get('DM') if (var.get('c').get(var.put('p',Js(var.get('p').to_number())-Js(1)))==var.get('k')) else var.get('Math').callprop('floor', ((var.get('c').get(var.get('p'))*var.get('m'))+((var.get('c').get((var.get('p')-Js(1.0)))+var.get('o'))*var.get('n'))))))
        if (var.get('c').put(var.get('p'), var.get('f').callprop('am', Js(0.0), var.get('s'), var.get('c'), var.get('q'), Js(0.0), var.get('j')), '+')<var.get('s')):
            var.get('f').callprop('dlShiftTo', var.get('q'), var.get('r'))
            var.get('c').callprop('subTo', var.get('r'), var.get('c'))
            while (var.get('c').get(var.get('p'))<var.put('s',Js(var.get('s').to_number())-Js(1))):
                var.get('c').callprop('subTo', var.get('r'), var.get('c'))
    if (var.get('b')!=var.get(u"null")):
        var.get('c').callprop('drShiftTo', var.get('j'), var.get('b'))
        if (var.get('g')!=var.get('h')):
            var.get('BigInteger').get('ZERO').callprop('subTo', var.get('b'), var.get('b'))
    var.get('c').put('t', var.get('j'))
    var.get('c').callprop('clamp')
    if (var.get('i')>Js(0.0)):
        var.get('c').callprop('rShiftTo', var.get('i'), var.get('c'))
    if (var.get('g')<Js(0.0)):
        var.get('BigInteger').get('ZERO').callprop('subTo', var.get('c'), var.get('c'))
PyJsHoisted_bnpDivRemTo_.func_name = 'bnpDivRemTo'
var.put('bnpDivRemTo', PyJsHoisted_bnpDivRemTo_)
@Js
def PyJsHoisted_bnpDRShiftTo_(a, b, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'b':b}, var)
    var.registers(['a', 'c', 'b'])
    #for JS loop
    var.put('c', var.get('a'))
    while (var.get('c')<var.get(u"this").get('t')):
        try:
            var.get('b').put((var.get('c')-var.get('a')), var.get(u"this").get(var.get('c')))
        finally:
                var.put('c',Js(var.get('c').to_number())+Js(1))
    var.get('b').put('t', var.get('Math').callprop('max', (var.get(u"this").get('t')-var.get('a')), Js(0.0)))
    var.get('b').put('s', var.get(u"this").get('s'))
PyJsHoisted_bnpDRShiftTo_.func_name = 'bnpDRShiftTo'
var.put('bnpDRShiftTo', PyJsHoisted_bnpDRShiftTo_)
@Js
def PyJsHoisted_get_encpw_(sessionkey, evalue, nvalue, id, pw, this, arguments, var=var):
    var = Scope({'sessionkey':sessionkey, 'evalue':evalue, 'arguments':arguments, 'pw':pw, 'this':this, 'nvalue':nvalue, 'id':id}, var)
    var.registers(['evalue', 'nvalue', 'pw', 'rsa', 'sessionkey', 'id'])
    var.put('rsa', var.get('RSAKey').create())
    var.get('rsa').callprop('setPublic', var.get('evalue'), var.get('nvalue'))
    return var.get('rsa').callprop('encrypt', (((((var.get('getLenChar')(var.get('sessionkey'))+var.get('sessionkey'))+var.get('getLenChar')(var.get('id')))+var.get('id'))+var.get('getLenChar')(var.get('pw')))+var.get('pw')))
PyJsHoisted_get_encpw_.func_name = 'get_encpw'
var.put('get_encpw', PyJsHoisted_get_encpw_)
@Js
def PyJsHoisted_intAt_(a, b, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'b':b}, var)
    var.registers(['a', 'c', 'b'])
    var.put('c', var.get('BI_RC').get(var.get('a').callprop('charCodeAt', var.get('b'))))
    return ((-Js(1.0)) if (var.get('c')==var.get(u"null")) else var.get('c'))
PyJsHoisted_intAt_.func_name = 'intAt'
var.put('intAt', PyJsHoisted_intAt_)
@Js
def PyJsHoisted_bnModPowInt_(a, b, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'b':b}, var)
    var.registers(['a', 'c', 'b'])
    pass
    if ((var.get('a')<Js(256.0)) or var.get('b').callprop('isEven')):
        var.put('c', var.get('Classic').create(var.get('b')))
    else:
        var.put('c', var.get('Montgomery').create(var.get('b')))
    return var.get(u"this").callprop('exp', var.get('a'), var.get('c'))
PyJsHoisted_bnModPowInt_.func_name = 'bnModPowInt'
var.put('bnModPowInt', PyJsHoisted_bnModPowInt_)
@Js
def PyJsHoisted_RSADoPublic_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['a'])
    return var.get('a').callprop('modPowInt', var.get(u"this").get('e'), var.get(u"this").get('n'))
PyJsHoisted_RSADoPublic_.func_name = 'RSADoPublic'
var.put('RSADoPublic', PyJsHoisted_RSADoPublic_)
@Js
def PyJsHoisted_bnpIsEven_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return (((var.get(u"this").get('0')&Js(1.0)) if (var.get(u"this").get('t')>Js(0.0)) else var.get(u"this").get('s'))==Js(0.0))
PyJsHoisted_bnpIsEven_.func_name = 'bnpIsEven'
var.put('bnpIsEven', PyJsHoisted_bnpIsEven_)
@Js
def PyJsHoisted_montConvert_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['b', 'a'])
    var.put('b', var.get('nbi')())
    var.get('a').callprop('abs').callprop('dlShiftTo', var.get(u"this").get('m').get('t'), var.get('b'))
    var.get('b').callprop('divRemTo', var.get(u"this").get('m'), var.get(u"null"), var.get('b'))
    if ((var.get('a').get('s')<Js(0.0)) and (var.get('b').callprop('compareTo', var.get('BigInteger').get('ZERO'))>Js(0.0))):
        var.get(u"this").get('m').callprop('subTo', var.get('b'), var.get('b'))
    return var.get('b')
PyJsHoisted_montConvert_.func_name = 'montConvert'
var.put('montConvert', PyJsHoisted_montConvert_)
@Js
def PyJsHoisted_am2_(a, b, c, d, e, f, this, arguments, var=var):
    var = Scope({'d':d, 'this':this, 'b':b, 'arguments':arguments, 'f':f, 'e':e, 'a':a, 'c':c}, var)
    var.registers(['d', 'b', 'f', 'e', 'j', 'a', 'c', 'i', 'k', 'h', 'g'])
    var.put('g', (var.get('b')&Js(32767.0)))
    var.put('h', (var.get('b')>>Js(15.0)))
    while (var.put('f',Js(var.get('f').to_number())-Js(1))>=Js(0.0)):
        var.put('i', (var.get(u"this").get(var.get('a'))&Js(32767.0)))
        var.put('j', (var.get(u"this").get((var.put('a',Js(var.get('a').to_number())+Js(1))-Js(1)))>>Js(15.0)))
        var.put('k', ((var.get('h')*var.get('i'))+(var.get('j')*var.get('g'))))
        var.put('i', ((((var.get('g')*var.get('i'))+((var.get('k')&Js(32767.0))<<Js(15.0)))+var.get('c').get(var.get('d')))+(var.get('e')&Js(1073741823.0))))
        var.put('e', (((PyJsBshift(var.get('i'),Js(30.0))+PyJsBshift(var.get('k'),Js(15.0)))+(var.get('h')*var.get('j')))+PyJsBshift(var.get('e'),Js(30.0))))
        var.get('c').put((var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1)), (var.get('i')&Js(1073741823.0)))
    return var.get('e')
PyJsHoisted_am2_.func_name = 'am2'
var.put('am2', PyJsHoisted_am2_)
@Js
def PyJsHoisted_montRevert_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['b', 'a'])
    var.put('b', var.get('nbi')())
    var.get('a').callprop('copyTo', var.get('b'))
    var.get(u"this").callprop('reduce', var.get('b'))
    return var.get('b')
PyJsHoisted_montRevert_.func_name = 'montRevert'
var.put('montRevert', PyJsHoisted_montRevert_)
@Js
def PyJsHoisted_ARC4next_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    pass
    var.get(u"this").put('i', ((var.get(u"this").get('i')+Js(1.0))&Js(255.0)))
    var.get(u"this").put('j', ((var.get(u"this").get('j')+var.get(u"this").get('S').get(var.get(u"this").get('i')))&Js(255.0)))
    var.put('a', var.get(u"this").get('S').get(var.get(u"this").get('i')))
    var.get(u"this").get('S').put(var.get(u"this").get('i'), var.get(u"this").get('S').get(var.get(u"this").get('j')))
    var.get(u"this").get('S').put(var.get(u"this").get('j'), var.get('a'))
    return var.get(u"this").get('S').get(((var.get('a')+var.get(u"this").get('S').get(var.get(u"this").get('i')))&Js(255.0)))
PyJsHoisted_ARC4next_.func_name = 'ARC4next'
var.put('ARC4next', PyJsHoisted_ARC4next_)
@Js
def PyJsHoisted_rng_seed_time_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get('rng_seed_int')(var.get('Date').create().callprop('getTime'))
PyJsHoisted_rng_seed_time_.func_name = 'rng_seed_time'
var.put('rng_seed_time', PyJsHoisted_rng_seed_time_)
@Js
def PyJsHoisted_nbv_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['b', 'a'])
    var.put('b', var.get('nbi')())
    var.get('b').callprop('fromInt', var.get('a'))
    return var.get('b')
PyJsHoisted_nbv_.func_name = 'nbv'
var.put('nbv', PyJsHoisted_nbv_)
@Js
def PyJsHoisted_bnpInvDigit_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b'])
    if (var.get(u"this").get('t')<Js(1.0)):
        return Js(0.0)
    var.put('a', var.get(u"this").get('0'))
    if ((var.get('a')&Js(1.0))==Js(0.0)):
        return Js(0.0)
    var.put('b', (var.get('a')&Js(3.0)))
    var.put('b', ((var.get('b')*(Js(2.0)-((var.get('a')&Js(15.0))*var.get('b'))))&Js(15.0)))
    var.put('b', ((var.get('b')*(Js(2.0)-((var.get('a')&Js(255.0))*var.get('b'))))&Js(255.0)))
    var.put('b', ((var.get('b')*(Js(2.0)-(((var.get('a')&Js(65535.0))*var.get('b'))&Js(65535.0))))&Js(65535.0)))
    var.put('b', ((var.get('b')*(Js(2.0)-((var.get('a')*var.get('b'))%var.get(u"this").get('DV'))))%var.get(u"this").get('DV')))
    return ((var.get(u"this").get('DV')-var.get('b')) if (var.get('b')>Js(0.0)) else (-var.get('b')))
PyJsHoisted_bnpInvDigit_.func_name = 'bnpInvDigit'
var.put('bnpInvDigit', PyJsHoisted_bnpInvDigit_)
@Js
def PyJsHoisted_bnpRShiftTo_(a, b, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'b':b}, var)
    var.registers(['d', 'b', 'f', 'e', 'a', 'c', 'g'])
    var.get('b').put('s', var.get(u"this").get('s'))
    var.put('c', var.get('Math').callprop('floor', (var.get('a')/var.get(u"this").get('DB'))))
    if (var.get('c')>=var.get(u"this").get('t')):
        var.get('b').put('t', Js(0.0))
        return var.get('undefined')
    var.put('d', (var.get('a')%var.get(u"this").get('DB')))
    var.put('e', (var.get(u"this").get('DB')-var.get('d')))
    var.put('f', ((Js(1.0)<<var.get('d'))-Js(1.0)))
    var.get('b').put('0', (var.get(u"this").get(var.get('c'))>>var.get('d')))
    #for JS loop
    var.put('g', (var.get('c')+Js(1.0)))
    while (var.get('g')<var.get(u"this").get('t')):
        try:
            var.get('b').put(((var.get('g')-var.get('c'))-Js(1.0)), ((var.get(u"this").get(var.get('g'))&var.get('f'))<<var.get('e')), '|')
            var.get('b').put((var.get('g')-var.get('c')), (var.get(u"this").get(var.get('g'))>>var.get('d')))
        finally:
                var.put('g',Js(var.get('g').to_number())+Js(1))
    if (var.get('d')>Js(0.0)):
        var.get('b').put(((var.get(u"this").get('t')-var.get('c'))-Js(1.0)), ((var.get(u"this").get('s')&var.get('f'))<<var.get('e')), '|')
    var.get('b').put('t', (var.get(u"this").get('t')-var.get('c')))
    var.get('b').callprop('clamp')
PyJsHoisted_bnpRShiftTo_.func_name = 'bnpRShiftTo'
var.put('bnpRShiftTo', PyJsHoisted_bnpRShiftTo_)
@Js
def PyJsHoisted_rng_get_bytes_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['b', 'a'])
    pass
    #for JS loop
    var.put('b', Js(0.0))
    while (var.get('b')<var.get('a').get('length')):
        try:
            var.get('a').put(var.get('b'), var.get('rng_get_byte')())
        finally:
                var.put('b',Js(var.get('b').to_number())+Js(1))
PyJsHoisted_rng_get_bytes_.func_name = 'rng_get_bytes'
var.put('rng_get_bytes', PyJsHoisted_rng_get_bytes_)
@Js
def PyJsHoisted_b64tohex_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['d', 'b', 'a', 'c', 'e'])
    var.put('b', Js(''))
    pass
    var.put('d', Js(0.0))
    pass
    #for JS loop
    var.put('c', Js(0.0))
    while (var.get('c')<var.get('a').get('length')):
        try:
            if (var.get('a').callprop('charAt', var.get('c'))==var.get('b64pad')):
                break
            var.put('v', var.get('b64map').callprop('indexOf', var.get('a').callprop('charAt', var.get('c'))))
            if (var.get('v')<Js(0.0)):
                continue
            if (var.get('d')==Js(0.0)):
                var.put('b', var.get('int2char')((var.get('v')>>Js(2.0))), '+')
                var.put('e', (var.get('v')&Js(3.0)))
                var.put('d', Js(1.0))
            else:
                if (var.get('d')==Js(1.0)):
                    var.put('b', var.get('int2char')(((var.get('e')<<Js(2.0))|(var.get('v')>>Js(4.0)))), '+')
                    var.put('e', (var.get('v')&Js(15.0)))
                    var.put('d', Js(2.0))
                else:
                    if (var.get('d')==Js(2.0)):
                        var.put('b', var.get('int2char')(var.get('e')), '+')
                        var.put('b', var.get('int2char')((var.get('v')>>Js(2.0))), '+')
                        var.put('e', (var.get('v')&Js(3.0)))
                        var.put('d', Js(3.0))
                    else:
                        var.put('b', var.get('int2char')(((var.get('e')<<Js(2.0))|(var.get('v')>>Js(4.0)))), '+')
                        var.put('b', var.get('int2char')((var.get('v')&Js(15.0))), '+')
                        var.put('d', Js(0.0))
        finally:
                var.put('c',Js(var.get('c').to_number())+Js(1))
    if (var.get('d')==Js(1.0)):
        var.put('b', var.get('int2char')((var.get('e')<<Js(2.0))), '+')
    return var.get('b')
PyJsHoisted_b64tohex_.func_name = 'b64tohex'
var.put('b64tohex', PyJsHoisted_b64tohex_)
@Js
def PyJsHoisted_nbits_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['b', 'a', 'c'])
    var.put('b', Js(1.0))
    if (var.put('c', PyJsBshift(var.get('a'),Js(16.0)))!=Js(0.0)):
        var.put('a', var.get('c'))
        var.put('b', Js(16.0), '+')
    if (var.put('c', (var.get('a')>>Js(8.0)))!=Js(0.0)):
        var.put('a', var.get('c'))
        var.put('b', Js(8.0), '+')
    if (var.put('c', (var.get('a')>>Js(4.0)))!=Js(0.0)):
        var.put('a', var.get('c'))
        var.put('b', Js(4.0), '+')
    if (var.put('c', (var.get('a')>>Js(2.0)))!=Js(0.0)):
        var.put('a', var.get('c'))
        var.put('b', Js(2.0), '+')
    if (var.put('c', (var.get('a')>>Js(1.0)))!=Js(0.0)):
        var.put('a', var.get('c'))
        var.put('b', Js(1.0), '+')
    return var.get('b')
PyJsHoisted_nbits_.func_name = 'nbits'
var.put('nbits', PyJsHoisted_nbits_)
@Js
def PyJsHoisted_cConvert_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['a'])
    if ((var.get('a').get('s')<Js(0.0)) or (var.get('a').callprop('compareTo', var.get(u"this").get('m'))>=Js(0.0))):
        return var.get('a').callprop('mod', var.get(u"this").get('m'))
    else:
        return var.get('a')
PyJsHoisted_cConvert_.func_name = 'cConvert'
var.put('cConvert', PyJsHoisted_cConvert_)
@Js
def PyJsHoisted_nbi_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return var.get('BigInteger').create(var.get(u"null"))
PyJsHoisted_nbi_.func_name = 'nbi'
var.put('nbi', PyJsHoisted_nbi_)
@Js
def PyJsHoisted_rng_get_byte_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    if (var.get('rng_state')==var.get(u"null")):
        var.get('rng_seed_time')()
        var.put('rng_state', var.get('prng_newstate')())
        var.get('rng_state').callprop('init', var.get('rng_pool'))
        #for JS loop
        var.put('rng_pptr', Js(0.0))
        while (var.get('rng_pptr')<var.get('rng_pool').get('length')):
            try:
                var.get('rng_pool').put(var.get('rng_pptr'), Js(0.0))
            finally:
                    var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))
        var.put('rng_pptr', Js(0.0))
    return var.get('rng_state').callprop('next')
PyJsHoisted_rng_get_byte_.func_name = 'rng_get_byte'
var.put('rng_get_byte', PyJsHoisted_rng_get_byte_)
@Js
def PyJsHoisted_bnpFromInt_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['a'])
    var.get(u"this").put('t', Js(1.0))
    var.get(u"this").put('s', ((-Js(1.0)) if (var.get('a')<Js(0.0)) else Js(0.0)))
    if (var.get('a')>Js(0.0)):
        var.get(u"this").put('0', var.get('a'))
    else:
        if (var.get('a')<(-Js(1.0))):
            var.get(u"this").put('0', (var.get('a')+var.get('DV')))
        else:
            var.get(u"this").put('t', Js(0.0))
PyJsHoisted_bnpFromInt_.func_name = 'bnpFromInt'
var.put('bnpFromInt', PyJsHoisted_bnpFromInt_)
@Js
def PyJsHoisted_SecureRandom_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    pass
PyJsHoisted_SecureRandom_.func_name = 'SecureRandom'
var.put('SecureRandom', PyJsHoisted_SecureRandom_)
@Js
def PyJsHoisted_bnAbs_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return (var.get(u"this").callprop('negate') if (var.get(u"this").get('s')<Js(0.0)) else var.get(u"this"))
PyJsHoisted_bnAbs_.func_name = 'bnAbs'
var.put('bnAbs', PyJsHoisted_bnAbs_)
@Js
def PyJsHoisted_bnMod_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['b', 'a'])
    var.put('b', var.get('nbi')())
    var.get(u"this").callprop('abs').callprop('divRemTo', var.get('a'), var.get(u"null"), var.get('b'))
    if ((var.get(u"this").get('s')<Js(0.0)) and (var.get('b').callprop('compareTo', var.get('BigInteger').get('ZERO'))>Js(0.0))):
        var.get('a').callprop('subTo', var.get('b'), var.get('b'))
    return var.get('b')
PyJsHoisted_bnMod_.func_name = 'bnMod'
var.put('bnMod', PyJsHoisted_bnMod_)
@Js
def PyJsHoisted_RSAKey_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get(u"this").put('n', var.get(u"null"))
    var.get(u"this").put('e', Js(0.0))
    var.get(u"this").put('d', var.get(u"null"))
    var.get(u"this").put('p', var.get(u"null"))
    var.get(u"this").put('q', var.get(u"null"))
    var.get(u"this").put('dmp1', var.get(u"null"))
    var.get(u"this").put('dmq1', var.get(u"null"))
    var.get(u"this").put('coeff', var.get(u"null"))
PyJsHoisted_RSAKey_.func_name = 'RSAKey'
var.put('RSAKey', PyJsHoisted_RSAKey_)
@Js
def PyJsHoisted_bnpMultiplyTo_(a, b, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'b':b}, var)
    var.registers(['d', 'a', 'c', 'e', 'b'])
    var.put('c', var.get(u"this").callprop('abs'))
    var.put('d', var.get('a').callprop('abs'))
    var.put('e', var.get('c').get('t'))
    var.get('b').put('t', (var.get('e')+var.get('d').get('t')))
    while (var.put('e',Js(var.get('e').to_number())-Js(1))>=Js(0.0)):
        var.get('b').put(var.get('e'), Js(0.0))
    #for JS loop
    var.put('e', Js(0.0))
    while (var.get('e')<var.get('d').get('t')):
        try:
            var.get('b').put((var.get('e')+var.get('c').get('t')), var.get('c').callprop('am', Js(0.0), var.get('d').get(var.get('e')), var.get('b'), var.get('e'), Js(0.0), var.get('c').get('t')))
        finally:
                var.put('e',Js(var.get('e').to_number())+Js(1))
    var.get('b').put('s', Js(0.0))
    var.get('b').callprop('clamp')
    if (var.get(u"this").get('s')!=var.get('a').get('s')):
        var.get('BigInteger').get('ZERO').callprop('subTo', var.get('b'), var.get('b'))
PyJsHoisted_bnpMultiplyTo_.func_name = 'bnpMultiplyTo'
var.put('bnpMultiplyTo', PyJsHoisted_bnpMultiplyTo_)
@Js
def PyJsHoisted_bnToString_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['d', 'b', 'f', 'e', 'a', 'c', 'h', 'g'])
    if (var.get(u"this").get('s')<Js(0.0)):
        return (Js('-')+var.get(u"this").callprop('negate').callprop('toString', var.get('a')))
    pass
    if (var.get('a')==Js(16.0)):
        var.put('b', Js(4.0))
    else:
        if (var.get('a')==Js(8.0)):
            var.put('b', Js(3.0))
        else:
            if (var.get('a')==Js(2.0)):
                var.put('b', Js(1.0))
            else:
                if (var.get('a')==Js(32.0)):
                    var.put('b', Js(5.0))
                else:
                    if (var.get('a')==Js(4.0)):
                        var.put('b', Js(2.0))
                    else:
                        return var.get(u"this").callprop('toRadix', var.get('a'))
    var.put('c', ((Js(1.0)<<var.get('b'))-Js(1.0)))
    var.put('e', Js(False))
    var.put('f', Js(''))
    var.put('g', var.get(u"this").get('t'))
    var.put('h', (var.get(u"this").get('DB')-((var.get('g')*var.get(u"this").get('DB'))%var.get('b'))))
    if ((var.put('g',Js(var.get('g').to_number())-Js(1))+Js(1))>Js(0.0)):
        if ((var.get('h')<var.get(u"this").get('DB')) and (var.put('d', (var.get(u"this").get(var.get('g'))>>var.get('h')))>Js(0.0))):
            var.put('e', Js(True))
            var.put('f', var.get('int2char')(var.get('d')))
        while (var.get('g')>=Js(0.0)):
            if (var.get('h')<var.get('b')):
                var.put('d', ((var.get(u"this").get(var.get('g'))&((Js(1.0)<<var.get('h'))-Js(1.0)))<<(var.get('b')-var.get('h'))))
                var.put('d', (var.get(u"this").get(var.put('g',Js(var.get('g').to_number())-Js(1)))>>var.put('h', (var.get(u"this").get('DB')-var.get('b')), '+')), '|')
            else:
                var.put('d', ((var.get(u"this").get(var.get('g'))>>var.put('h', var.get('b'), '-'))&var.get('c')))
                if (var.get('h')<=Js(0.0)):
                    var.put('h', var.get(u"this").get('DB'), '+')
                    var.put('g',Js(var.get('g').to_number())-Js(1))
            if (var.get('d')>Js(0.0)):
                var.put('e', Js(True))
            if var.get('e'):
                var.put('f', var.get('int2char')(var.get('d')), '+')
    return (var.get('f') if var.get('e') else Js('0'))
PyJsHoisted_bnToString_.func_name = 'bnToString'
var.put('bnToString', PyJsHoisted_bnToString_)
@Js
def PyJsHoisted_pkcs1pad2_(a, b, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'b':b}, var)
    var.registers(['d', 'a', 'c', 'b'])
    if (var.get('b')<(var.get('a').get('length')+Js(11.0))):
        var.get('alert')(Js('Message too long for RSA'))
        return var.get(u"null")
    var.put('c', var.get('Array').create())
    var.put('d', (var.get('a').get('length')-Js(1.0)))
    while ((var.get('d')>=Js(0.0)) and (var.get('b')>Js(0.0))):
        var.get('c').put(var.put('b',Js(var.get('b').to_number())-Js(1)), var.get('a').callprop('charCodeAt', (var.put('d',Js(var.get('d').to_number())-Js(1))+Js(1))))
    var.get('c').put(var.put('b',Js(var.get('b').to_number())-Js(1)), Js(0.0))
    while (var.get('b')>Js(2.0)):
        var.get('c').put(var.put('b',Js(var.get('b').to_number())-Js(1)), var.get('Math').callprop('floor', (Js(1.0)+(var.get('Math').callprop('random')*Js(254.99)))))
    var.get('c').put(var.put('b',Js(var.get('b').to_number())-Js(1)), Js(2.0))
    var.get('c').put(var.put('b',Js(var.get('b').to_number())-Js(1)), Js(0.0))
    return var.get('BigInteger').create(var.get('c'))
PyJsHoisted_pkcs1pad2_.func_name = 'pkcs1pad2'
var.put('pkcs1pad2', PyJsHoisted_pkcs1pad2_)
@Js
def PyJsHoistedNonPyName(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b'])
    var.put('a', Js([]))
    #for JS loop
    var.put('b', Js(0.0))
    while (var.get('b')<var.get('arguments').get('length')):
        try:
            if (var.get('arguments').get(var.get('b')).typeof()==Js('string')):
                var.get('a').put(var.get('a').get('length'), var.get('document').callprop('getElementById', var.get('arguments').get(var.get('b'))))
            else:
                var.get('a').put(var.get('a').get('length'), var.get('arguments').get(var.get('b')))
        finally:
                (var.put('b',Js(var.get('b').to_number())+Js(1))-Js(1))
    return (var.get('a') if var.get('a').get('1') else var.get('a').get('0'))
PyJsHoistedNonPyName.func_name = '$'
var.put('$', PyJsHoistedNonPyName)
@Js
def PyJsHoisted_BigInteger_(a, b, c, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'c':c, 'b':b}, var)
    var.registers(['a', 'c', 'b'])
    if (var.get('a')!=var.get(u"null")):
        if (Js('number')==var.get('a',throw=False).typeof()):
            var.get(u"this").callprop('fromNumber', var.get('a'), var.get('b'), var.get('c'))
        else:
            if ((var.get('b')==var.get(u"null")) and (Js('string')!=var.get('a',throw=False).typeof())):
                var.get(u"this").callprop('fromString', var.get('a'), Js(256.0))
            else:
                var.get(u"this").callprop('fromString', var.get('a'), var.get('b'))
PyJsHoisted_BigInteger_.func_name = 'BigInteger'
var.put('BigInteger', PyJsHoisted_BigInteger_)
@Js
def PyJsHoisted_prng_newstate_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    return var.get('Arcfour').create()
PyJsHoisted_prng_newstate_.func_name = 'prng_newstate'
var.put('prng_newstate', PyJsHoisted_prng_newstate_)
@Js
def PyJsHoisted_cReduce_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['a'])
    var.get('a').callprop('divRemTo', var.get(u"this").get('m'), var.get(u"null"), var.get('a'))
PyJsHoisted_cReduce_.func_name = 'cReduce'
var.put('cReduce', PyJsHoisted_cReduce_)
@Js
def PyJsHoisted_montReduce_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['d', 'b', 'a', 'c'])
    while (var.get('a').get('t')<=var.get(u"this").get('mt2')):
        var.get('a').put((var.get('a').put('t',Js(var.get('a').get('t').to_number())+Js(1))-Js(1)), Js(0.0))
    #for JS loop
    var.put('b', Js(0.0))
    while (var.get('b')<var.get(u"this").get('m').get('t')):
        try:
            var.put('c', (var.get('a').get(var.get('b'))&Js(32767.0)))
            var.put('d', (((var.get('c')*var.get(u"this").get('mpl'))+((((var.get('c')*var.get(u"this").get('mph'))+((var.get('a').get(var.get('b'))>>Js(15.0))*var.get(u"this").get('mpl')))&var.get(u"this").get('um'))<<Js(15.0)))&var.get('a').get('DM')))
            var.put('c', (var.get('b')+var.get(u"this").get('m').get('t')))
            var.get('a').put(var.get('c'), var.get(u"this").get('m').callprop('am', Js(0.0), var.get('d'), var.get('a'), var.get('b'), Js(0.0), var.get(u"this").get('m').get('t')), '+')
            while (var.get('a').get(var.get('c'))>=var.get('a').get('DV')):
                var.get('a').put(var.get('c'), var.get('a').get('DV'), '-')
                (var.get('a').put(var.put('c',Js(var.get('c').to_number())+Js(1)),Js(var.get('a').get(var.put('c',Js(var.get('c').to_number())+Js(1))).to_number())+Js(1))-Js(1))
        finally:
                var.put('b',Js(var.get('b').to_number())+Js(1))
    var.get('a').callprop('clamp')
    var.get('a').callprop('drShiftTo', var.get(u"this").get('m').get('t'), var.get('a'))
    if (var.get('a').callprop('compareTo', var.get(u"this").get('m'))>=Js(0.0)):
        var.get('a').callprop('subTo', var.get(u"this").get('m'), var.get('a'))
PyJsHoisted_montReduce_.func_name = 'montReduce'
var.put('montReduce', PyJsHoisted_montReduce_)
@Js
def PyJsHoisted_byte2Hex_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['a'])
    if (var.get('a')<Js(16.0)):
        return (Js('0')+var.get('a').callprop('toString', Js(16.0)))
    else:
        return var.get('a').callprop('toString', Js(16.0))
PyJsHoisted_byte2Hex_.func_name = 'byte2Hex'
var.put('byte2Hex', PyJsHoisted_byte2Hex_)
@Js
def PyJsHoisted_bnpCopyTo_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['b', 'a'])
    #for JS loop
    var.put('b', (var.get(u"this").get('t')-Js(1.0)))
    while (var.get('b')>=Js(0.0)):
        try:
            var.get('a').put(var.get('b'), var.get(u"this").get(var.get('b')))
        finally:
                var.put('b',Js(var.get('b').to_number())-Js(1))
    var.get('a').put('t', var.get(u"this").get('t'))
    var.get('a').put('s', var.get(u"this").get('s'))
PyJsHoisted_bnpCopyTo_.func_name = 'bnpCopyTo'
var.put('bnpCopyTo', PyJsHoisted_bnpCopyTo_)
@Js
def PyJsHoisted_bnpSquareTo_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['d', 'b', 'a', 'c'])
    var.put('b', var.get(u"this").callprop('abs'))
    var.put('c', var.get('a').put('t', (Js(2.0)*var.get('b').get('t'))))
    while (var.put('c',Js(var.get('c').to_number())-Js(1))>=Js(0.0)):
        var.get('a').put(var.get('c'), Js(0.0))
    #for JS loop
    var.put('c', Js(0.0))
    while (var.get('c')<(var.get('b').get('t')-Js(1.0))):
        try:
            var.put('d', var.get('b').callprop('am', var.get('c'), var.get('b').get(var.get('c')), var.get('a'), (Js(2.0)*var.get('c')), Js(0.0), Js(1.0)))
            if (var.get('a').put((var.get('c')+var.get('b').get('t')), var.get('b').callprop('am', (var.get('c')+Js(1.0)), (Js(2.0)*var.get('b').get(var.get('c'))), var.get('a'), ((Js(2.0)*var.get('c'))+Js(1.0)), var.get('d'), ((var.get('b').get('t')-var.get('c'))-Js(1.0))), '+')>=var.get('b').get('DV')):
                var.get('a').put((var.get('c')+var.get('b').get('t')), var.get('b').get('DV'), '-')
                var.get('a').put(((var.get('c')+var.get('b').get('t'))+Js(1.0)), Js(1.0))
        finally:
                var.put('c',Js(var.get('c').to_number())+Js(1))
    if (var.get('a').get('t')>Js(0.0)):
        var.get('a').put((var.get('a').get('t')-Js(1.0)), var.get('b').callprop('am', var.get('c'), var.get('b').get(var.get('c')), var.get('a'), (Js(2.0)*var.get('c')), Js(0.0), Js(1.0)), '+')
    var.get('a').put('s', Js(0.0))
    var.get('a').callprop('clamp')
PyJsHoisted_bnpSquareTo_.func_name = 'bnpSquareTo'
var.put('bnpSquareTo', PyJsHoisted_bnpSquareTo_)
@Js
def PyJsHoisted_cRevert_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['a'])
    return var.get('a')
PyJsHoisted_cRevert_.func_name = 'cRevert'
var.put('cRevert', PyJsHoisted_cRevert_)
@Js
def PyJsHoisted_bnpDLShiftTo_(a, b, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'b':b}, var)
    var.registers(['a', 'c', 'b'])
    pass
    #for JS loop
    var.put('c', (var.get(u"this").get('t')-Js(1.0)))
    while (var.get('c')>=Js(0.0)):
        try:
            var.get('b').put((var.get('c')+var.get('a')), var.get(u"this").get(var.get('c')))
        finally:
                var.put('c',Js(var.get('c').to_number())-Js(1))
    #for JS loop
    var.put('c', (var.get('a')-Js(1.0)))
    while (var.get('c')>=Js(0.0)):
        try:
            var.get('b').put(var.get('c'), Js(0.0))
        finally:
                var.put('c',Js(var.get('c').to_number())-Js(1))
    var.get('b').put('t', (var.get(u"this").get('t')+var.get('a')))
    var.get('b').put('s', var.get(u"this").get('s'))
PyJsHoisted_bnpDLShiftTo_.func_name = 'bnpDLShiftTo'
var.put('bnpDLShiftTo', PyJsHoisted_bnpDLShiftTo_)
@Js
def PyJsHoisted_RSAEncrypt_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['d', 'b', 'a', 'c', 'e'])
    var.put('b', var.get('pkcs1pad2')(var.get('a'), ((var.get(u"this").get('n').callprop('bitLength')+Js(7.0))>>Js(3.0))))
    if (var.get('b')==var.get(u"null")):
        return var.get(u"null")
    var.put('c', var.get(u"this").callprop('doPublic', var.get('b')))
    if (var.get('c')==var.get(u"null")):
        return var.get(u"null")
    var.put('d', var.get('c').callprop('toString', Js(16.0)))
    var.put('e', ((((var.get(u"this").get('n').callprop('bitLength')+Js(7.0))>>Js(3.0))<<Js(1.0))-var.get('d').get('length')))
    while ((var.put('e',Js(var.get('e').to_number())-Js(1))+Js(1))>Js(0.0)):
        var.put('d', (Js('0')+var.get('d')))
    return var.get('d')
PyJsHoisted_RSAEncrypt_.func_name = 'RSAEncrypt'
var.put('RSAEncrypt', PyJsHoisted_RSAEncrypt_)
@Js
def PyJsHoisted_hex2b64_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['d', 'b', 'a', 'c'])
    pass
    pass
    var.put('d', Js(''))
    #for JS loop
    var.put('b', Js(0.0))
    while ((var.get('b')+Js(3.0))<=var.get('a').get('length')):
        try:
            var.put('c', var.get('parseInt')(var.get('a').callprop('substring', var.get('b'), (var.get('b')+Js(3.0))), Js(16.0)))
            var.put('d', (var.get('b64map').callprop('charAt', (var.get('c')>>Js(6.0)))+var.get('b64map').callprop('charAt', (var.get('c')&Js(63.0)))), '+')
        finally:
                var.put('b', Js(3.0), '+')
    if ((var.get('b')+Js(1.0))==var.get('a').get('length')):
        var.put('c', var.get('parseInt')(var.get('a').callprop('substring', var.get('b'), (var.get('b')+Js(1.0))), Js(16.0)))
        var.put('d', var.get('b64map').callprop('charAt', (var.get('c')<<Js(2.0))), '+')
    else:
        if ((var.get('b')+Js(2.0))==var.get('a').get('length')):
            var.put('c', var.get('parseInt')(var.get('a').callprop('substring', var.get('b'), (var.get('b')+Js(2.0))), Js(16.0)))
            var.put('d', (var.get('b64map').callprop('charAt', (var.get('c')>>Js(2.0)))+var.get('b64map').callprop('charAt', ((var.get('c')&Js(3.0))<<Js(4.0)))), '+')
    while ((var.get('d').get('length')&Js(3.0))>Js(0.0)):
        var.put('d', var.get('b64pad'), '+')
    return var.get('d')
PyJsHoisted_hex2b64_.func_name = 'hex2b64'
var.put('hex2b64', PyJsHoisted_hex2b64_)
@Js
def PyJsHoisted_bnBitLength_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    if (var.get(u"this").get('t')<=Js(0.0)):
        return Js(0.0)
    return ((var.get(u"this").get('DB')*(var.get(u"this").get('t')-Js(1.0)))+var.get('nbits')((var.get(u"this").get((var.get(u"this").get('t')-Js(1.0)))^(var.get(u"this").get('s')&var.get(u"this").get('DM')))))
PyJsHoisted_bnBitLength_.func_name = 'bnBitLength'
var.put('bnBitLength', PyJsHoisted_bnBitLength_)
@Js
def PyJsHoisted_bnpLShiftTo_(a, b, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'b':b}, var)
    var.registers(['d', 'b', 'f', 'e', 'a', 'c', 'h', 'g'])
    var.put('c', (var.get('a')%var.get(u"this").get('DB')))
    var.put('d', (var.get(u"this").get('DB')-var.get('c')))
    var.put('e', ((Js(1.0)<<var.get('d'))-Js(1.0)))
    var.put('f', var.get('Math').callprop('floor', (var.get('a')/var.get(u"this").get('DB'))))
    var.put('g', ((var.get(u"this").get('s')<<var.get('c'))&var.get(u"this").get('DM')))
    #for JS loop
    var.put('h', (var.get(u"this").get('t')-Js(1.0)))
    while (var.get('h')>=Js(0.0)):
        try:
            var.get('b').put(((var.get('h')+var.get('f'))+Js(1.0)), ((var.get(u"this").get(var.get('h'))>>var.get('d'))|var.get('g')))
            var.put('g', ((var.get(u"this").get(var.get('h'))&var.get('e'))<<var.get('c')))
        finally:
                var.put('h',Js(var.get('h').to_number())-Js(1))
    #for JS loop
    var.put('h', (var.get('f')-Js(1.0)))
    while (var.get('h')>=Js(0.0)):
        try:
            var.get('b').put(var.get('h'), Js(0.0))
        finally:
                var.put('h',Js(var.get('h').to_number())-Js(1))
    var.get('b').put(var.get('f'), var.get('g'))
    var.get('b').put('t', ((var.get(u"this").get('t')+var.get('f'))+Js(1.0)))
    var.get('b').put('s', var.get(u"this").get('s'))
    var.get('b').callprop('clamp')
PyJsHoisted_bnpLShiftTo_.func_name = 'bnpLShiftTo'
var.put('bnpLShiftTo', PyJsHoisted_bnpLShiftTo_)
@Js
def PyJsHoisted_ARC4init_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['d', 'b', 'a', 'c'])
    pass
    #for JS loop
    var.put('b', Js(0.0))
    while (var.get('b')<Js(256.0)):
        try:
            var.get(u"this").get('S').put(var.get('b'), var.get('b'))
        finally:
                var.put('b',Js(var.get('b').to_number())+Js(1))
    var.put('c', Js(0.0))
    #for JS loop
    var.put('b', Js(0.0))
    while (var.get('b')<Js(256.0)):
        try:
            var.put('c', (((var.get('c')+var.get(u"this").get('S').get(var.get('b')))+var.get('a').get((var.get('b')%var.get('a').get('length'))))&Js(255.0)))
            var.put('d', var.get(u"this").get('S').get(var.get('b')))
            var.get(u"this").get('S').put(var.get('b'), var.get(u"this").get('S').get(var.get('c')))
            var.get(u"this").get('S').put(var.get('c'), var.get('d'))
        finally:
                var.put('b',Js(var.get('b').to_number())+Js(1))
    var.get(u"this").put('i', Js(0.0))
    var.get(u"this").put('j', Js(0.0))
PyJsHoisted_ARC4init_.func_name = 'ARC4init'
var.put('ARC4init', PyJsHoisted_ARC4init_)
@Js
def PyJsHoisted_bnpExp_(a, b, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'b':b}, var)
    var.registers(['d', 'b', 'f', 'e', 'a', 'c', 'g'])
    if ((var.get('a')>Js(4294967295.0)) or (var.get('a')<Js(1.0))):
        return var.get('BigInteger').get('ONE')
    var.put('c', var.get('nbi')())
    var.put('d', var.get('nbi')())
    var.put('e', var.get('b').callprop('convert', var.get(u"this")))
    var.put('f', (var.get('nbits')(var.get('a'))-Js(1.0)))
    var.get('e').callprop('copyTo', var.get('c'))
    while (var.put('f',Js(var.get('f').to_number())-Js(1))>=Js(0.0)):
        var.get('b').callprop('sqrTo', var.get('c'), var.get('d'))
        if ((var.get('a')&(Js(1.0)<<var.get('f')))>Js(0.0)):
            var.get('b').callprop('mulTo', var.get('d'), var.get('e'), var.get('c'))
        else:
            var.put('g', var.get('c'))
            var.put('c', var.get('d'))
            var.put('d', var.get('g'))
    return var.get('b').callprop('revert', var.get('c'))
PyJsHoisted_bnpExp_.func_name = 'bnpExp'
var.put('bnpExp', PyJsHoisted_bnpExp_)
@Js
def PyJsHoisted_linebrk_(a, b, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'b':b}, var)
    var.registers(['d', 'a', 'c', 'b'])
    var.put('c', Js(''))
    var.put('d', Js(0.0))
    while ((var.get('d')+var.get('b'))<var.get('a').get('length')):
        var.put('c', (var.get('a').callprop('substring', var.get('d'), (var.get('d')+var.get('b')))+Js('\n')), '+')
        var.put('d', var.get('b'), '+')
    return (var.get('c')+var.get('a').callprop('substring', var.get('d'), var.get('a').get('length')))
PyJsHoisted_linebrk_.func_name = 'linebrk'
var.put('linebrk', PyJsHoisted_linebrk_)
@Js
def PyJsHoisted_montSqrTo_(a, b, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'b':b}, var)
    var.registers(['a', 'b'])
    var.get('a').callprop('squareTo', var.get('b'))
    var.get(u"this").callprop('reduce', var.get('b'))
PyJsHoisted_montSqrTo_.func_name = 'montSqrTo'
var.put('montSqrTo', PyJsHoisted_montSqrTo_)
@Js
def PyJsHoisted_montMulTo_(a, b, c, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'c':c, 'b':b}, var)
    var.registers(['a', 'c', 'b'])
    var.get('a').callprop('multiplyTo', var.get('b'), var.get('c'))
    var.get(u"this").callprop('reduce', var.get('c'))
PyJsHoisted_montMulTo_.func_name = 'montMulTo'
var.put('montMulTo', PyJsHoisted_montMulTo_)
@Js
def PyJsHoisted_int2char_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['a'])
    return var.get('BI_RM').callprop('charAt', var.get('a'))
PyJsHoisted_int2char_.func_name = 'int2char'
var.put('int2char', PyJsHoisted_int2char_)
@Js
def PyJsHoisted_bnNegate_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    var.put('a', var.get('nbi')())
    var.get('BigInteger').get('ZERO').callprop('subTo', var.get(u"this"), var.get('a'))
    return var.get('a')
PyJsHoisted_bnNegate_.func_name = 'bnNegate'
var.put('bnNegate', PyJsHoisted_bnNegate_)
@Js
def PyJsHoisted_bnCompareTo_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['b', 'a', 'c'])
    var.put('b', (var.get(u"this").get('s')-var.get('a').get('s')))
    if (var.get('b')!=Js(0.0)):
        return var.get('b')
    var.put('c', var.get(u"this").get('t'))
    var.put('b', (var.get('c')-var.get('a').get('t')))
    if (var.get('b')!=Js(0.0)):
        return var.get('b')
    while (var.put('c',Js(var.get('c').to_number())-Js(1))>=Js(0.0)):
        if (var.put('b', (var.get(u"this").get(var.get('c'))-var.get('a').get(var.get('c'))))!=Js(0.0)):
            return var.get('b')
    return Js(0.0)
PyJsHoisted_bnCompareTo_.func_name = 'bnCompareTo'
var.put('bnCompareTo', PyJsHoisted_bnCompareTo_)
@Js
def PyJsHoisted_cSqrTo_(a, b, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'b':b}, var)
    var.registers(['a', 'b'])
    var.get('a').callprop('squareTo', var.get('b'))
    var.get(u"this").callprop('reduce', var.get('b'))
PyJsHoisted_cSqrTo_.func_name = 'cSqrTo'
var.put('cSqrTo', PyJsHoisted_cSqrTo_)
@Js
def PyJsHoisted_rng_seed_int_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['a'])
    var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), (var.get('a')&Js(255.0)), '^')
    var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), ((var.get('a')>>Js(8.0))&Js(255.0)), '^')
    var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), ((var.get('a')>>Js(16.0))&Js(255.0)), '^')
    var.get('rng_pool').put((var.put('rng_pptr',Js(var.get('rng_pptr').to_number())+Js(1))-Js(1)), ((var.get('a')>>Js(24.0))&Js(255.0)), '^')
    if (var.get('rng_pptr')>=var.get('rng_psize')):
        var.put('rng_pptr', var.get('rng_psize'), '-')
PyJsHoisted_rng_seed_int_.func_name = 'rng_seed_int'
var.put('rng_seed_int', PyJsHoisted_rng_seed_int_)
@Js
def PyJsHoisted_bnpSubTo_(a, b, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'b':b}, var)
    var.registers(['d', 'a', 'c', 'e', 'b'])
    var.put('c', Js(0.0))
    var.put('d', Js(0.0))
    var.put('e', var.get('Math').callprop('min', var.get('a').get('t'), var.get(u"this").get('t')))
    while (var.get('c')<var.get('e')):
        var.put('d', (var.get(u"this").get(var.get('c'))-var.get('a').get(var.get('c'))), '+')
        var.get('b').put((var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1)), (var.get('d')&var.get(u"this").get('DM')))
        var.put('d', var.get(u"this").get('DB'), '>>')
    if (var.get('a').get('t')<var.get(u"this").get('t')):
        var.put('d', var.get('a').get('s'), '-')
        while (var.get('c')<var.get(u"this").get('t')):
            var.put('d', var.get(u"this").get(var.get('c')), '+')
            var.get('b').put((var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1)), (var.get('d')&var.get(u"this").get('DM')))
            var.put('d', var.get(u"this").get('DB'), '>>')
        var.put('d', var.get(u"this").get('s'), '+')
    else:
        var.put('d', var.get(u"this").get('s'), '+')
        while (var.get('c')<var.get('a').get('t')):
            var.put('d', var.get('a').get(var.get('c')), '-')
            var.get('b').put((var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1)), (var.get('d')&var.get(u"this").get('DM')))
            var.put('d', var.get(u"this").get('DB'), '>>')
        var.put('d', var.get('a').get('s'), '-')
    var.get('b').put('s', ((-Js(1.0)) if (var.get('d')<Js(0.0)) else Js(0.0)))
    if (var.get('d')<(-Js(1.0))):
        var.get('b').put((var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1)), (var.get(u"this").get('DV')+var.get('d')))
    else:
        if (var.get('d')>Js(0.0)):
            var.get('b').put((var.put('c',Js(var.get('c').to_number())+Js(1))-Js(1)), var.get('d'))
    var.get('b').put('t', var.get('c'))
    var.get('b').callprop('clamp')
PyJsHoisted_bnpSubTo_.func_name = 'bnpSubTo'
var.put('bnpSubTo', PyJsHoisted_bnpSubTo_)
@Js
def PyJsHoisted_clearErrorLayers_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['error', 'errors'])
    var.put('errors', var.get('Array').create(Js('err_empty_captcha'), Js('err_autologin'), Js('err_network_delay'), Js('err_unsupport_browser'), Js('err_empty_id'), Js('err_empty_pw'), Js('err_idpw_incorrect'), Js('err_grpidpw_incorrect')))
    for PyJsTemp in var.get('errors'):
        var.put('error', PyJsTemp)
        var.put('e', var.get('$')(var.get('error')))
        if (var.get('e')!=var.get(u"null")):
            var.get('e').get('style').put('display', Js('none'))
PyJsHoisted_clearErrorLayers_.func_name = 'clearErrorLayers'
var.put('clearErrorLayers', PyJsHoisted_clearErrorLayers_)
@Js
def PyJsHoisted_am1_(a, b, c, d, e, f, this, arguments, var=var):
    var = Scope({'d':d, 'this':this, 'b':b, 'arguments':arguments, 'f':f, 'e':e, 'a':a, 'c':c}, var)
    var.registers(['d', 'b', 'f', 'e', 'a', 'c', 'g'])
    while (var.put('f',Js(var.get('f').to_number())-Js(1))>=Js(0.0)):
        var.put('g', (((var.get('b')*var.get(u"this").get((var.put('a',Js(var.get('a').to_number())+Js(1))-Js(1))))+var.get('c').get(var.get('d')))+var.get('e')))
        var.put('e', var.get('Math').callprop('floor', (var.get('g')/Js(67108864.0))))
        var.get('c').put((var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1)), (var.get('g')&Js(67108863.0)))
    return var.get('e')
PyJsHoisted_am1_.func_name = 'am1'
var.put('am1', PyJsHoisted_am1_)
@Js
def PyJsHoisted_keySplit_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['a'])
    var.put('keys', var.get('a').callprop('split', Js(',')))
    if ((((var.get('a').neg() or var.get('keys').get('0').neg()) or var.get('keys').get('1').neg()) or var.get('keys').get('2').neg()) or var.get('keys').get('3').neg()):
        return Js(False)
    var.put('sessionkey', var.get('keys').get('0'))
    var.put('keyname', var.get('keys').get('1'))
    var.put('evalue', var.get('keys').get('2'))
    var.put('nvalue', var.get('keys').get('3'))
    var.get('$')(Js('encnm')).put('value', var.get('keyname'))
    return Js(True)
PyJsHoisted_keySplit_.func_name = 'keySplit'
var.put('keySplit', PyJsHoisted_keySplit_)
@Js
def PyJsHoisted_cMulTo_(a, b, c, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'c':c, 'b':b}, var)
    var.registers(['a', 'c', 'b'])
    var.get('a').callprop('multiplyTo', var.get('b'), var.get('c'))
    var.get(u"this").callprop('reduce', var.get('c'))
PyJsHoisted_cMulTo_.func_name = 'cMulTo'
var.put('cMulTo', PyJsHoisted_cMulTo_)
@Js
def PyJsHoisted_bnpClamp_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['a'])
    var.put('a', (var.get(u"this").get('s')&var.get(u"this").get('DM')))
    while ((var.get(u"this").get('t')>Js(0.0)) and (var.get(u"this").get((var.get(u"this").get('t')-Js(1.0)))==var.get('a'))):
        var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())-Js(1))
PyJsHoisted_bnpClamp_.func_name = 'bnpClamp'
var.put('bnpClamp', PyJsHoisted_bnpClamp_)
@Js
def PyJsHoisted_RSASetPublic_(a, b, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'b':b}, var)
    var.registers(['a', 'b'])
    if ((((var.get('a')!=var.get(u"null")) and (var.get('b')!=var.get(u"null"))) and (var.get('a').get('length')>Js(0.0))) and (var.get('b').get('length')>Js(0.0))):
        var.get(u"this").put('n', var.get('parseBigInt')(var.get('a'), Js(16.0)))
        var.get(u"this").put('e', var.get('parseInt')(var.get('b'), Js(16.0)))
    else:
        var.get('alert')(Js('Invalid RSA public key'))
PyJsHoisted_RSASetPublic_.func_name = 'RSASetPublic'
var.put('RSASetPublic', PyJsHoisted_RSASetPublic_)
@Js
def PyJsHoisted_Classic_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['a'])
    var.get(u"this").put('m', var.get('a'))
PyJsHoisted_Classic_.func_name = 'Classic'
var.put('Classic', PyJsHoisted_Classic_)
@Js
def PyJsHoisted_parseBigInt_(a, b, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'b':b}, var)
    var.registers(['a', 'b'])
    return var.get('BigInteger').create(var.get('a'), var.get('b'))
PyJsHoisted_parseBigInt_.func_name = 'parseBigInt'
var.put('parseBigInt', PyJsHoisted_parseBigInt_)
@Js
def PyJsHoisted_am3_(a, b, c, d, e, f, this, arguments, var=var):
    var = Scope({'d':d, 'this':this, 'b':b, 'arguments':arguments, 'f':f, 'e':e, 'a':a, 'c':c}, var)
    var.registers(['d', 'b', 'f', 'e', 'j', 'a', 'c', 'i', 'k', 'h', 'g'])
    var.put('g', (var.get('b')&Js(16383.0)))
    var.put('h', (var.get('b')>>Js(14.0)))
    while (var.put('f',Js(var.get('f').to_number())-Js(1))>=Js(0.0)):
        var.put('i', (var.get(u"this").get(var.get('a'))&Js(16383.0)))
        var.put('j', (var.get(u"this").get((var.put('a',Js(var.get('a').to_number())+Js(1))-Js(1)))>>Js(14.0)))
        var.put('k', ((var.get('h')*var.get('i'))+(var.get('j')*var.get('g'))))
        var.put('i', ((((var.get('g')*var.get('i'))+((var.get('k')&Js(16383.0))<<Js(14.0)))+var.get('c').get(var.get('d')))+var.get('e')))
        var.put('e', (((var.get('i')>>Js(28.0))+(var.get('k')>>Js(14.0)))+(var.get('h')*var.get('j'))))
        var.get('c').put((var.put('d',Js(var.get('d').to_number())+Js(1))-Js(1)), (var.get('i')&Js(268435455.0)))
    return var.get('e')
PyJsHoisted_am3_.func_name = 'am3'
var.put('am3', PyJsHoisted_am3_)
@Js
def PyJsHoisted_Montgomery_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['a'])
    var.get(u"this").put('m', var.get('a'))
    var.get(u"this").put('mp', var.get('a').callprop('invDigit'))
    var.get(u"this").put('mpl', (var.get(u"this").get('mp')&Js(32767.0)))
    var.get(u"this").put('mph', (var.get(u"this").get('mp')>>Js(15.0)))
    var.get(u"this").put('um', ((Js(1.0)<<(var.get('a').get('DB')-Js(15.0)))-Js(1.0)))
    var.get(u"this").put('mt2', (Js(2.0)*var.get('a').get('t')))
PyJsHoisted_Montgomery_.func_name = 'Montgomery'
var.put('Montgomery', PyJsHoisted_Montgomery_)
@Js
def PyJsHoisted_Arcfour_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers([])
    var.get(u"this").put('i', Js(0.0))
    var.get(u"this").put('j', Js(0.0))
    var.get(u"this").put('S', var.get('Array').create())
PyJsHoisted_Arcfour_.func_name = 'Arcfour'
var.put('Arcfour', PyJsHoisted_Arcfour_)
@Js
def PyJsHoisted_getLenChar_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['a'])
    var.put('a', (var.get('a')+Js('')))
    return var.get('String').callprop('fromCharCode', var.get('a').get('length'))
PyJsHoisted_getLenChar_.func_name = 'getLenChar'
var.put('getLenChar', PyJsHoisted_getLenChar_)
@Js
def PyJsHoisted_bnpFromString_(a, b, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments, 'b':b}, var)
    var.registers(['d', 'b', 'f', 'e', 'a', 'c', 'g'])
    pass
    if (var.get('b')==Js(16.0)):
        var.put('c', Js(4.0))
    else:
        if (var.get('b')==Js(8.0)):
            var.put('c', Js(3.0))
        else:
            if (var.get('b')==Js(256.0)):
                var.put('c', Js(8.0))
            else:
                if (var.get('b')==Js(2.0)):
                    var.put('c', Js(1.0))
                else:
                    if (var.get('b')==Js(32.0)):
                        var.put('c', Js(5.0))
                    else:
                        if (var.get('b')==Js(4.0)):
                            var.put('c', Js(2.0))
                        else:
                            var.get(u"this").callprop('fromRadix', var.get('a'), var.get('b'))
                            return var.get('undefined')
    var.get(u"this").put('t', Js(0.0))
    var.get(u"this").put('s', Js(0.0))
    var.put('d', var.get('a').get('length'))
    var.put('e', Js(False))
    var.put('f', Js(0.0))
    while (var.put('d',Js(var.get('d').to_number())-Js(1))>=Js(0.0)):
        var.put('g', ((var.get('a').get(var.get('d'))&Js(255.0)) if (var.get('c')==Js(8.0)) else var.get('intAt')(var.get('a'), var.get('d'))))
        if (var.get('g')<Js(0.0)):
            if (var.get('a').callprop('charAt', var.get('d'))==Js('-')):
                var.put('e', Js(True))
            continue
        var.put('e', Js(False))
        if (var.get('f')==Js(0.0)):
            var.get(u"this").put((var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())+Js(1))-Js(1)), var.get('g'))
        else:
            if ((var.get('f')+var.get('c'))>var.get(u"this").get('DB')):
                var.get(u"this").put((var.get(u"this").get('t')-Js(1.0)), ((var.get('g')&((Js(1.0)<<(var.get(u"this").get('DB')-var.get('f')))-Js(1.0)))<<var.get('f')), '|')
                var.get(u"this").put((var.get(u"this").put('t',Js(var.get(u"this").get('t').to_number())+Js(1))-Js(1)), (var.get('g')>>(var.get(u"this").get('DB')-var.get('f'))))
            else:
                var.get(u"this").put((var.get(u"this").get('t')-Js(1.0)), (var.get('g')<<var.get('f')), '|')
        var.put('f', var.get('c'), '+')
        if (var.get('f')>=var.get(u"this").get('DB')):
            var.put('f', var.get(u"this").get('DB'), '-')
    if ((var.get('c')==Js(8.0)) and ((var.get('a').get('0')&Js(128.0))!=Js(0.0))):
        var.get(u"this").put('s', (-Js(1.0)))
        if (var.get('f')>Js(0.0)):
            var.get(u"this").put((var.get(u"this").get('t')-Js(1.0)), (((Js(1.0)<<(var.get(u"this").get('DB')-var.get('f')))-Js(1.0))<<var.get('f')), '|')
    var.get(u"this").callprop('clamp')
    if var.get('e'):
        var.get('BigInteger').get('ZERO').callprop('subTo', var.get(u"this"), var.get(u"this"))
PyJsHoisted_bnpFromString_.func_name = 'bnpFromString'
var.put('bnpFromString', PyJsHoisted_bnpFromString_)
@Js
def PyJsHoisted_b64toBA_(a, this, arguments, var=var):
    var = Scope({'this':this, 'a':a, 'arguments':arguments}, var)
    var.registers(['d', 'b', 'a', 'c'])
    var.put('b', var.get('b64tohex')(var.get('a')))
    pass
    var.put('d', var.get('Array').create())
    #for JS loop
    var.put('c', Js(0.0))
    while ((Js(2.0)*var.get('c'))<var.get('b').get('length')):
        try:
            var.get('d').put(var.get('c'), var.get('parseInt')(var.get('b').callprop('substring', (Js(2.0)*var.get('c')), ((Js(2.0)*var.get('c'))+Js(2.0))), Js(16.0)))
        finally:
                var.put('c',Js(var.get('c').to_number())+Js(1))
    return var.get('d')
PyJsHoisted_b64toBA_.func_name = 'b64toBA'
var.put('b64toBA', PyJsHoisted_b64toBA_)
pass
var.put('dbits', Js(28.0))
var.get('BigInteger').get('prototype').put('am', var.get('am3'))
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
var.put('canary', Js(244837814094590))
var.put('j_lm', ((var.get('canary')&Js(16777215.0))==Js(15715070.0)))
var.get('BigInteger').get('prototype').put('DB', var.get('dbits'))
var.get('BigInteger').get('prototype').put('DM', ((Js(1.0)<<var.get('dbits'))-Js(1.0)))
var.get('BigInteger').get('prototype').put('DV', (Js(1.0)<<var.get('dbits')))
var.put('BI_FP', Js(52.0))
var.get('BigInteger').get('prototype').put('FV', var.get('Math').callprop('pow', Js(2.0), var.get('BI_FP')))
var.get('BigInteger').get('prototype').put('F1', (var.get('BI_FP')-var.get('dbits')))
var.get('BigInteger').get('prototype').put('F2', ((Js(2.0)*var.get('dbits'))-var.get('BI_FP')))
var.put('BI_RM', Js('0123456789abcdefghijklmnopqrstuvwxyz'))
var.put('BI_RC', var.get('Array').create())
pass
var.put('rr', Js('0').callprop('charCodeAt', Js(0.0)))
#for JS loop
var.put('vv', Js(0.0))
while (var.get('vv')<=Js(9.0)):
    try:
        var.get('BI_RC').put((var.put('rr',Js(var.get('rr').to_number())+Js(1))-Js(1)), var.get('vv'))
    finally:
            var.put('vv',Js(var.get('vv').to_number())+Js(1))
var.put('rr', Js('a').callprop('charCodeAt', Js(0.0)))
#for JS loop
var.put('vv', Js(10.0))
while (var.get('vv')<Js(36.0)):
    try:
        var.get('BI_RC').put((var.put('rr',Js(var.get('rr').to_number())+Js(1))-Js(1)), var.get('vv'))
    finally:
            var.put('vv',Js(var.get('vv').to_number())+Js(1))
var.put('rr', Js('A').callprop('charCodeAt', Js(0.0)))
#for JS loop
var.put('vv', Js(10.0))
while (var.get('vv')<Js(36.0)):
    try:
        var.get('BI_RC').put((var.put('rr',Js(var.get('rr').to_number())+Js(1))-Js(1)), var.get('vv'))
    finally:
            var.put('vv',Js(var.get('vv').to_number())+Js(1))
var.get('Classic').get('prototype').put('convert', var.get('cConvert'))
var.get('Classic').get('prototype').put('revert', var.get('cRevert'))
var.get('Classic').get('prototype').put('reduce', var.get('cReduce'))
var.get('Classic').get('prototype').put('mulTo', var.get('cMulTo'))
var.get('Classic').get('prototype').put('sqrTo', var.get('cSqrTo'))
var.get('Montgomery').get('prototype').put('convert', var.get('montConvert'))
var.get('Montgomery').get('prototype').put('revert', var.get('montRevert'))
var.get('Montgomery').get('prototype').put('reduce', var.get('montReduce'))
var.get('Montgomery').get('prototype').put('mulTo', var.get('montMulTo'))
var.get('Montgomery').get('prototype').put('sqrTo', var.get('montSqrTo'))
var.get('BigInteger').get('prototype').put('copyTo', var.get('bnpCopyTo'))
var.get('BigInteger').get('prototype').put('fromInt', var.get('bnpFromInt'))
var.get('BigInteger').get('prototype').put('fromString', var.get('bnpFromString'))
var.get('BigInteger').get('prototype').put('clamp', var.get('bnpClamp'))
var.get('BigInteger').get('prototype').put('dlShiftTo', var.get('bnpDLShiftTo'))
var.get('BigInteger').get('prototype').put('drShiftTo', var.get('bnpDRShiftTo'))
var.get('BigInteger').get('prototype').put('lShiftTo', var.get('bnpLShiftTo'))
var.get('BigInteger').get('prototype').put('rShiftTo', var.get('bnpRShiftTo'))
var.get('BigInteger').get('prototype').put('subTo', var.get('bnpSubTo'))
var.get('BigInteger').get('prototype').put('multiplyTo', var.get('bnpMultiplyTo'))
var.get('BigInteger').get('prototype').put('squareTo', var.get('bnpSquareTo'))
var.get('BigInteger').get('prototype').put('divRemTo', var.get('bnpDivRemTo'))
var.get('BigInteger').get('prototype').put('invDigit', var.get('bnpInvDigit'))
var.get('BigInteger').get('prototype').put('isEven', var.get('bnpIsEven'))
var.get('BigInteger').get('prototype').put('exp', var.get('bnpExp'))
var.get('BigInteger').get('prototype').put('toString', var.get('bnToString'))
var.get('BigInteger').get('prototype').put('negate', var.get('bnNegate'))
var.get('BigInteger').get('prototype').put('abs', var.get('bnAbs'))
var.get('BigInteger').get('prototype').put('compareTo', var.get('bnCompareTo'))
var.get('BigInteger').get('prototype').put('bitLength', var.get('bnBitLength'))
var.get('BigInteger').get('prototype').put('mod', var.get('bnMod'))
var.get('BigInteger').get('prototype').put('modPowInt', var.get('bnModPowInt'))
var.get('BigInteger').put('ZERO', var.get('nbv')(Js(0.0)))
var.get('BigInteger').put('ONE', var.get('nbv')(Js(1.0)))
var.get('Arcfour').get('prototype').put('init', var.get('ARC4init'))
var.get('Arcfour').get('prototype').put('next', var.get('ARC4next'))
var.get('RSAKey').get('prototype').put('doPublic', var.get('RSADoPublic'))
var.get('RSAKey').get('prototype').put('setPublic', var.get('RSASetPublic'))
var.get('RSAKey').get('prototype').put('encrypt', var.get('RSAEncrypt'))
var.put('b64map', Js('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'))
var.put('b64pad', Js('='))
pass
pass


# Add lib to the module scope
storefarm_common_all_trans = var.to_python()