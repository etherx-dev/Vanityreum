#!/usr/bin/env python
# coding=utf8

# Bitcoin Address Generation
# Copyright (C) 2015  Antoine FERRON
#
# Pure Python address generator
#
# Random source for key generation :
# CryptGenRandom in Windows
# /dev/urandom   in Unix-like
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 3 of the License.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

from lib.ECDSA_BTC import *
import hashlib

def hashrand(num):
	#return sha256 of num times 256bits random data
	rng_data=''
	for idat in xrange(num):
		rng_data = rng_data + os.urandom(32)
	assert len(rng_data) == num*32
	return hashlib.sha256(rng_data).hexdigest()

def randomforkey():
	candint = 0
	r = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141L
	while candint<1 or candint>=r:
		cand=hashrand(1024)
		candint=int(cand,16)
	return candint

print "\nGenerate new Bitcoin address from random"
load_gtable('lib/G_Table')
privkeynum = randomforkey()
pubkey = Public_key( generator_256, mulG(privkeynum) )
pubkey58 = pub_hex_base58(pubkey.point.x(),pubkey.point.y())
privkey = Private_key( pubkey, privkeynum )
print "\nAddress :  %s \n" % pubkey58
print "PrivKey :  %s" % priv_hex_base58(privkeynum)
