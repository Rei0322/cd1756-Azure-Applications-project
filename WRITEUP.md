# Write-up

### Analyze, choose, and justify the appropriate resource option for deploying the app.

**Costs**

Honestly, cost is where these two options look the most similar on paper but behave pretty differently in practice. A VM bills for the compute itself (per hour, based on size), and that's it from Azure's side — but I'd also be responsible for the OS, patching, and setting up whatever web server/reverse proxy the Flask app needs to actually be reachable, which is time I'd rather spend on the app. App Service bundles the web server and OS management into the price, so a comparable low-tier plan (Basic B1, for example) ends up cheap for a project this size, and I'm not paying for anything I have to configure myself.

**Scalability**

App Service has scaling built in — I can bump the plan tier or turn on autoscale rules without touching the app itself. A VM can scale too, but it means setting up a Virtual Machine Scale Set and a load balancer myself, which is a lot of extra infrastructure for a project that's realistically only ever going to see me and a grader hitting it.

**Availability**

Similar story — App Service gives me a published SLA and handles the underlying host for me. With a VM, if that one instance goes down, so does my app, unless I build out redundancy (multiple VMs, load balancing) on my own.

**Workflow**

This is the one that made the decision for me. App Service has a Deployment Center that connects directly to a GitHub repo — I can push a commit and have it deployed without touching FTP or manually copying files. A VM would mean I'm SSHing/RDPing in, installing dependencies, and manually managing the app process every time something changes.

**My choice**

I'm going with **App Service**. For a Flask app like this one, with no unusual OS-level dependencies, App Service gives me everything I need (hosting, scaling, GitHub-based deployment) without the operational overhead of managing a VM myself.

### Assess app changes that would change your decision.

If this app needed something App Service's sandboxed environment doesn't support — like a specific system-level driver, root access, custom networking configuration, or software that has to be installed at the OS level rather than through pip — I'd have to move to a VM, since that's the only option that gives me full control over the machine. Similarly, if this were becoming a long-running production app with unpredictable, spiky traffic and I needed very fine-grained control over the exact infrastructure (custom load balancing logic, specific VM extensions, etc.), that level of control might be worth the added management overhead of a VM. But for this project, none of that applies.

### Submission screenshots

All required proof screenshots have been uploaded to the `example_images/` folder, replacing the original sample images and keeping the same filenames so each one is easy to match to its requirement:

- `article-cms-solution.png` — the "Hello World!" article created on the deployed app
- `azure-portal-resource-group.png` — full Resource Group contents
- `blob-solution.png` — Blob storage endpoint URL
- `log-solution.png` — Log stream showing an invalid login attempt and a successful one
- `sql-storage-solution.png` — populated `users`/`posts` tables with a query result
- `uri-redirects-solution.png` — the redirect URI on the app registration
