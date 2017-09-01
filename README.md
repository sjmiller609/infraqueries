## backend

### how to set up development environment

```
git clone this repository
```

```
git checkout feature/serverless
```

```
vagrant up # turns on VM
```
wait ~5 min while the tech stack builds

```
vagrant ssh # enter the VM
cd /vagrant/src/infraqueries/vmstatus
```

```
source activate.sh # this will activate the environment on your shell
```

there is a file called 'service.py'. this is where the service is. 'event.json' is the sample input we can test with. let's run a test.

```
lambda invoke -v
```

this runs the lambda function once locally, returning the output of a function in service.py

in service.py take a look at the function "handler". this function returns a json payload if the user has a valid key.

just modify the function to return whatever you want. then...

```
lambda invoke -v
```

... to test the output.

if it looks satisfactory, you will want to deploy this to the production site.

paste the access credentials that I emailed you into the shell.

```
export AWS_ACCESS_KEY_ID=****************
export AWS_SECRET_ACCESS_KEY=****************
```

then deploy the function to AWS lambda service.

```
lambda deploy
```

the link below calls the deployed function, and is the URL you will call from the front end

### [call function](https://0o5eza3v7a.execute-api.us-west-2.amazonaws.com/prod/vmstatus?access_key=0000&secret_key=0000)


