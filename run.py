import vocabchallenge

if __name__ == '__main__':
	vocabchallenge.app.secret_key = 'development_key'
	vocabchallenge.app.run(debug=True)