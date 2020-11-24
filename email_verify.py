#!/usr/bin/env python
# coding: utf-8

import re,json,sys,requests

hunterapikey = "72813c40cf4bdd267980bf2df394c161d85f5599"

def VerificarEmail(email):
	r = requests.get("https://api.hunter.io/v2/email-verifier?email="+email+"&api_key="+hunterapikey)
	return (r.json())

def main():
	arquivo = open('emails.txt', 'r')
	emails_validos = open('emails_validos.txt', 'a')
	for line in arquivo:
		result = VerificarEmail(line)
		if result['errors'][0]['code'] == 429:
			print("(+) Acabou suas requests kkkkkkk")

		elif result['status'] == "valid":
			print("(+) Email válido: "+result['email'])
			content = emails_validos.writelines(line)
		else:
			print("(+) Error na API")
	arquivo.close()
	emails_validos.close()
main()
