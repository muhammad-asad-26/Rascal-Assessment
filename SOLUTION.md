Part 2 Solution:

I would introduce Celery Beat, Celery Worker and Redis to handle the cronjobs of sending out reminders to user emails for ending of their subscriptions.
The cronjob would run every day at 1 AM UTC time and scan through the database, user_subscriptions table to be specific and extract all the end dates of subscriptions that are ending in the next 24 hours.
Once extracted, it would trigger an email using Celery Worker, which we can extract the user's full_name and email columns for each user to remind them of the ending subscription. Once the email to the user is dispatched, i would update the last_notified field in the user_subscriptions table to the current time. to avoid spamming user with emails. Currently last_notified does not exist in the database schema, so i would add it to the user_subscriptions table.
And incase the subscription is not renewed within 24 hours of the email notification, the subscription status will be updated to EXPIRED and the user will no longer be able to access the premium features. This would also be handled in the same cronjob logic, where we will check if the subscription is expired or not and if it is, we will update the status to EXPIRED and the user will no longer be able to access the premium features.


Part 3 Security and handover:

3a: Data security
- Currently due to time constraint i did not implement password encryption. This will be done using bcrypt to encrypt user passwords, when the user signs-up, the password will be encrypted and stored in the database. When the user logs in, they will send their password and we will use bcrypte.checkpassword method to see if the incoming password is correct, without having to decrypt the stored database password.

- Use JWT tokens with expiry time of 24 hours to ensure the endpoints are secured and users cannot access the system without a valid token. Also to add refresh tokens to allow users to get a new access token without having to log in again.

- Implement rate limiting on the endpoints to prevent brute force attacks and other malicious activities.


3b: Handover to a non-technical manager

A good handover means the office manager can keep things running day to day without having to ping a developer for every little thing.
So you need a plain-English operations guide. Just the stuff they’ll actually do—adding a new member, checking a subscription, seeing who signed up for an event. No jargon. Screenshots where they help.

All the login details go in one secure place, like 1Password. Not in an email chain. Not in a Word doc on someone’s desktop.

Also spell out what not to touch, and why. Say: don’t edit the database directly. Don’t rotate API keys without a developer in the loop. Most things break because someone tried to help but changed the wrong thing.

And finally, name one developer they can contact when something isn’t in the guide. A handover without a contact isn’t a handover—it’s just a document.
