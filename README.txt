Lazy messenger

Descriptioin:   Messenger web app
MORE: 		Enable registered users to share Text messages, Images and Videos


For Dev

Important:
	Admin account should not have a profile, Login in to use as a normal user will pop an error.
	beffore starting project:
		run 'makemigrations & migrate to prep database'
		create a superuser admin account
		run server on your prfered ip address

	If an error occur, debug to fix it.
	More features are to be appended, tip in anything if possible
	Added features should not affect available features

For Users

HOW TO
	1. Create Account
		On first page 📄, choose 'Create Account AnonymousUser'
		Provide your username and password, Profile image is required
		you will be redirected to login page, user informations that you provided on creating account.

	2. Creating Chat
		On first use, Chat list is empty. Open globe 🌐 select any user to start chat with
		Chat page will automatically open, then knok your self out
		
	3. Sharing files
		Just before message input area there is a bowtie click upon it and select whatsoever you want to share

	4. Error handling
		If Internal server errors occur, page not found, message wont load logout then login again
		When sharing large files page will take a lot of time to load. cancel the process, wait or choose small file

		