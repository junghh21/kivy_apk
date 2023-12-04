# Actions


Caching
You can set up cache for Buildozer global and local directories. Global directory is in root of repository. Local directory is in workdir.

Global: .buildozer-global (sdk, ndk, platform-tools)
Local: test_app/.buildozer (dependencies, build temp, not recommended to cache)
I don't recommend to cache local buildozer directory because Buildozer doesn't automatically update dependencies to latest version.

Use cache only if it speeds up your workflow! Usually this only adds 1-3 minutes to job running time, so I don't use it.

Example:
```
- name: Cache Buildozer global directory
  uses: actions/cache@v2
  with:
    path: .buildozer_global
    key: buildozer-global-${{ hashFiles('test_app/buildozer.spec') }} # Replace with your path
```
Location
<repository>/.github/workflows

Workflow file
 - workflow run if the workflow file (the YAML file in .github/workflows) is on the default branch (usually main)
 - YAML
 - Workflow files have a specific syntax
 - one or more jobs (run in parallel on Runners)
 - start conditions specified in the workflow
 - The on keyword and the lines that follow it define which types of triggers the workflow will match on and start executing
   respond to a single event
   on: push
   respond to a list (multiple events)
   on: [push, pull_request]
   respond to event types with qualifiers, such as branches, tags, or file paths
   on:
     push:
       branches:
         - main
         - 'rel/v*'
       tags:
         - v1.*
         - beta
       paths:
         - '**.ts'
   execute on a specific schedule or interval (using standard cron syntax)
   on:
     scheduled:
       - cron: '30 5,15 * * *'
   respond to specific manual events
   on: [workflow-dispatch, repository-dispatch]
   be called from other workflows (referred to as a reuse event)
   on: workflow_call
   respond to common activities on GitHub items, such as adding a comment to a GitHub issue
   on: issue_comment
   
Job
 - building, testing, and packaging
 - Jobs are made up of steps
 - runners are defined for jobs
   jobs:
     build:
       runs-on: ubuntu-latest
       steps:
         - uses: actions/checkout@v3
         - name: setup Go version'
           uses: actions/setup-go@v2
             with:
               go-version: '1.14.0'
         - run: go run helloworld.go
   
Step
 - A step either runs a shell command or invokes a predefined GitHub action
 - steps in a job are executed on a runner (The runner is a server, (virtual or physical))
   run : shell commands are executed
   uses : any predefined actions
   with : arguments/parameters to pass to the action
   - : a step starts
   steps:
     - uses: actions/checkout@v3
     - name: setup Go version
       uses: actions/setup-go@v2
       with:
         go-version: '1.14.0'
     - run: go run helloworld.go

![image](https://github.com/junghh21/Actions/assets/6457248/1c5d81eb-7528-41f1-a258-3a62c309acbf)
