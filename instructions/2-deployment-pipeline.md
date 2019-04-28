# Exercise 2: Configure your Deployment Pipeline

## Goals

* Learn about [GoCD](https://www.gocd.org/)
* Configure a [Deployment Pipeline](https://martinfowler.com/bliki/DeploymentPipeline.html)
to build and deploy your application to production
* Test the application running in production

## Step by Step instructions

We have provisioned all the infrastructure required for the workshop. Each
participant is assigned a numeric ID (from 1 to 50), which will be used
throughout the workshop.

1. Go to GoCD at http://gocd.cd4ml.net and login with the username and password
provided.

2. Click on the little gear symbol (![gear](./images/gear.png)) next to
`ci-workshop-app-X` to edit your deployment pipeline configuration.

3. Go to the *"Materials"* tab and edit the existing GitHub URL so that it
points to your forked repository URL - probably just replacing `ThoughtWorksInc`
with your GitHub username.

4. Save and go back to the [Dashboard](http://gocd.cd4ml.net) page

5. Make a small change to your forked code, e.g., change the `README.md`, then
add, commit, and push your changes to see your project being built and deployed
in GoCD:
```bash
git add .
git commit -m"Sample change"
git push
```

6. Once the pipeline succeeds, you can access your application's URL at
http://userX.app.cd4ml.net (replace `X` with your user ID)

7. Done! Go to [the next exercise](./3-machine-learning-pipeline.md)
