## <u>Identifying the problem</u>

1. **<u>Security</u>:** In my app i tried to impliment robust and thorough security and authentication measures, to ensure user data is not open to any other than themselves (and admins) trying to emulate, at a basic level platforms like [Steam](https://store.steampowered.com/) or [Origin](https://www.ea.com/en-au/games/library/pc-download). Trying to ensure safety of all users.

2. **<u>Community</U>:** Enabling reviews, helps other users decide what games they would like to purchase and encourages community engagement. 

### <u>Why solve this problem</u>



**Security** and **community engagement** are critical aspects for online game store platforms due to their profound impact on user trust, platform reputation, and overall success:

#### <u>Security</u>:

1. **<u>Data Protection</u>:** Online game stores collect and store sensitive user information, including personal data, payment details, and gaming preferences. A security breach can lead to data theft, identity theft, and financial losses for users, which we can see increasingly each year and perhaps also at greater scale in the online world.

2. **<u>Trust and Reputation</u>:** Security incidents erode user trust and damage the platform's reputation. Users are less likely to use a platform with a history of security vulnerabilities or data breaches.

3. **<u>Legal and Compliance</u>:** Failure to implement robust security measures can result in legal and regulatory consequences. Data protection laws require platforms to safeguard user data.


#### <u>Community</u>

1. **<u>User Engagement</u>:** Engaged users are more likely to stay on the platform, make purchases, and contribute positively to the community. Encouraging community engagement can lead to increased user retention.

2. **<u>Feedback and Improvement</u>:** User feedback through reviews and discussions can help game developers and platform administrators identify areas for improvement, fix bugs, and enhance the gaming experience.

3. **<u>Moderation</u>:** Maintaining a healthy community requires moderation to prevent toxic behavior, hate speech, and harassment. Failure to manage community interactions can result in a negative environment that drives users away.

### <u>Selecting PostgreSQL as the Database System</u>

The decision to utilize PostgreSQL as the database system for this project stems from the main following reasons:

#### 1. **<u>Robust Relational Database</u>:**
- PostgreSQL is a robust and mature relational database system known for its reliability and data integrity. It offers a solid foundation for managing structured data, which is crucial for the online game store's core functionalities.

#### 2. **<u>Personal knowledge</u>:** 
- Postgresql is the dbms i am most familiar with, using it through out course work made it a go to choice for something on the more basic level.

### <u>Drawbacks to other DBMS</u>

While PostgreSQL offers numerous benefits, it's important to acknowledge potential drawbacks compared to alternative database systems:

#### 
1. **<u>Resource Usage</u>:** 
- PostgreSQL can be resource-intensive, especially for large and complex databases. It can consume significant memory and CPU resources, which may not be suitable for projects with limited resources or those running on small machines. For such cases, more lightweight database options like SQLite or MySQL could be considered.

2. **<u>Scaling Challenges</u>:** 
- PostgreSQL does have the capability to scale vertically, meaning it can be upgraded with more powerful hardware to handle increased workloads. However, it's worth noting that there are certain limitations to vertical scaling, and at some point, further hardware upgrades might become impractical.

- Scaling PostgreSQL horizontally, which means adding more servers to handle increased loads, can be more complex and may demand advanced expertise compared to certain NoSQL databases that offer built-in support for easy horizontal scaling.

### <u>Functions and benefits of ORMs</u>

1. **<u>Code reuseability</u>:**
- ORM facilitates the reusability of code by providing pre-built components for interacting with the database. Developers can utilize these ready-made elements across different parts of their application, resulting in significant time savings and the prevention of code repetition.

2. **<u>Straight forward operations</u>:**
- ORMs offer innate support for the fundamental Create, Read, Update, and Delete (CRUD) operations. This simplifies the execution of common database actions without the need to craft intricate SQL code. Developers can focus on application logic rather than grappling with database intricacies.

3. **<u>Relationship Management</u>:**
- ORMs excel in simplifying the management of relationships between database tables, such as one-to-many or many-to-many associations. By working with objects and collections, developers can abstract the complexities of underlying join operations. This abstraction streamlines the handling of complex data relationships within the application, enhancing its overall maintainability and readability.




