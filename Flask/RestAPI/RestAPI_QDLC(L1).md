# Gayatri Dunkahe
# Wave2-B1-Python
# RestAPI_QDLC(L1)

1. What does REST API stand for?
- The REST API stand for - Representational State Transfer Application Programming Interface

2. Why do we use REST APIs?
- The REST APIs use for communicate over the internet using HTTP methods (GET, POST, PUT, DELETE) to perform operations on resources (e.g., data or services). 
- REST APIs used because they are simple, flexible, scalable, and widely adopted for building web services and enabling communication between different software applications. 
- They are easy to work with, platform-independent, and perform well, making them a popular choice in the world of web development.

3. What is the main purpose of a REST API?
- The main purpose of a REST API is to provide a standardized and efficient way for software systems to communicate, exchange data, and access resources over the internet, promoting simplicity, interoperability, and scalability in the process.

4. How do REST APIs communicate?
- The REST APIs communicate over the internet using HTTP methods (GET, POST, PUT, DELETE)

5. What are the key features of REST APIs?
- Statelessness: REST APIs are stateless, meaning that each request is independent and contains all necessary information.
- Client-Server Architecture: REST enforces a separation between client and server responsibilities.
- Resource-Based Design: Resources, identified by URLs, are central to the design of RESTful APIs.
- Uniform Interface: REST APIs use a consistent set of HTTP methods and status codes for interaction.
- Representation of Resources: Resources can be represented in various formats, enhancing flexibility.
- Stateless Communication: Requests and responses are self-contained, without the need for server-side state.

6. What are the common actions performed with REST APIs?
- Common actions performed with REST APIs include:
    - GET: Retrieve data or information from the server.
    - POST: Create a new resource on the server.
    - PUT: Update an existing resource on the server.
    - DELETE: Remove a resource from the server.

7. What does "stateless" mean in the context of REST?
- In the context of REST, "stateless" means that each request from a client to the server must contain all the information needed for the server to understand and process the request. 
- The server does not retain any information about the client's previous requests or state between requests. 
- This design simplifies server-side logic, enhances scalability, and allows requests to be processed independently.

8. What role does the URI play in REST APIs?
- URLs (Uniform Resource Locators), play a crucial role in REST APIs. 
- They serve as the unique identifiers for resources (e.g., data objects, services) and are used in HTTP requests to specify the resource being accessed or manipulated. 
- URIs define the address and path to a resource, making it possible for clients to locate and interact with resources on the server.

9. How is data typically formatted in REST APIs?
- Data in REST APIs is typically formatted using common data serialization formats such as JSON (JavaScript Object Notation) or XML (eXtensible Markup Language). 
These formats provide a structured way to represent data in a human-readable and machine-readable format. JSON is particularly popular due to its simplicity and widespread support in modern programming languages.

10. How is authentication managed in REST APIs?
- API Keys: Clients include an API key in the HTTP headers or query parameters of their requests to authenticate themselves with the server.
- OAuth: OAuth is a protocol for delegated authorization, allowing clients to obtain access tokens to access protected resources on behalf of a user or application.
- JWT (JSON Web Tokens): JWTs are compact and self-contained tokens that can be used for authentication and authorization. They are often used in token-based authentication systems.
- Basic Authentication: Clients include a username and password in the request headers (Base64-encoded) for authentication. However, this method is considered less secure for API access and is often used in combination with HTTPS.
- Bearer Token: A bearer token, often included in the "Authorization" header, provides proof of authentication. The server validates the token to grant or deny access to the requested resource.

11. What are HTTP status codes used for in REST API responses?
- HTTP status codes in REST API responses convey the outcome of a request.
- They provide information about whether the request was successful, encountered an error, or requires further action. Common status codes include:
    - 200 OK: The request was successful.
    - 201 Created: A new resource was successfully created.
    - 204 No Content: The request was successful, but there is no response body.
    - 400 Bad Request: The request is malformed or invalid.
    - 401 Unauthorized: Authentication is required or authentication failed.
    - 404 Not Found: The requested resource was not found.
    - 500 Internal Server Error: An unexpected error occurred on the server.

12. How can you handle errors in REST API responses?
- Errors in REST API responses are typically handled by including an error response format, often in JSON or XML, that provides details about the error. 
- This format may include an error code, a human-readable error message, and additional information to help diagnose and resolve the issue. 
- Additionally, appropriate HTTP status codes (e.g., 400 for client errors, 500 for server errors) should be used to indicate the nature of the error.

13. What's the difference between REST and SOAP?
- REST -
    - Representational State Transfer
    - It's an architectural style that uses standard HTTP methods and is based on the principles of simplicity, statelessness, and a resource-centric approach.
    - It typically uses lightweight data formats like JSON and is known for its flexibility and ease of use.
    - It is a lightweight and well-suited for simple web services

- SOAP -
    - Simple Object Access Protocol
    - It is a protocol that defines a strict set of rules for structuring messages and is typically transported over various protocols, including HTTP. 
    - It uses XML as its message format and is known for its strictness and support for advanced features like security and transactions.
    - It is a heavyweight and appropriate for complex enterprise-level services.

14. What is content negotiation in REST?
- Content negotiation in REST refers to the process by which the client and server agree on the format of data to be exchanged in an HTTP request and response. 
- It allows clients to request data in a specific format, such as JSON or XML, by specifying the desired content type in the request headers (e.g., "Accept: application/json").
- The server, in turn, uses this information to provide the response data in the requested format. 
- Content negotiation enhances flexibility by allowing clients and servers to communicate using the data format that best suits their needs.

15. How is versioning handled in REST APIs?
- Versioning in REST APIs is essential to ensure backward compatibility when making changes to the API. 
- There are several common approaches to handling versioning:
    - URI Versioning: Include the API version in the URI, e.g., /v1/resource. This approach is straightforward but can clutter the URI.
    - Header Versioning: Specify the API version in a custom HTTP header, such as Accept-Version or Api-Version. This keeps the URI cleaner but requires clients to set the header.
    - Media Type Versioning: Use different media types (e.g., application/vnd.myapi.v1+json) to indicate the version. This approach keeps the URI clean but may require more complex media type management.
    - No Versioning: Avoid versioning and ensure backward compatibility through careful API design and the use of features like default behavior or deprecation notices.

16. Why is hypermedia important in RESTful design?
- Hypermedia, or HATEOAS (Hypertext as the Engine of Application State), is important in RESTful design because it enables the dynamic discovery of available actions and resources within an API. - With hypermedia, clients can navigate the API's capabilities without relying on prior knowledge or hardcoding URLs. This makes the API more flexible, maintainable, and evolvable, as changes to resource relationships or endpoints can be handled dynamically by the client. Hypermedia also promotes a uniform and self-descriptive interface, aligning with REST's principles.

17. What is the Richardson Maturity Model?
- The Richardson Maturity Model is a model developed by `Leonard Richardson` that classifies the levels of RESTful maturity in web services based on their adherence to REST principles. 
- It has four levels:
    - Level 0: "The Swamp of POX" - At this level, the API uses HTTP as a transport mechanism but doesn't follow REST principles. It relies on a single URL for all operations.
    - Level 1: "Resources" - At this level, the API starts to use resources (e.g., URLs) to represent data, which is a fundamental REST concept.
    - Level 2: "HTTP Verbs" - At this level, the API uses HTTP methods (GET, POST, PUT, DELETE) to perform CRUD (Create, Read, Update, Delete) operations on resources.
    - Level 3: "Hypermedia Controls" (HATEOAS) - At the highest level, the API provides hypermedia controls in responses, allowing clients to dynamically navigate the API's capabilities

18. How can you ensure security in REST APIs?
- Authentication: Use methods like API keys, OAuth, JWT, or Basic Authentication to verify the identity of clients.
- Authorization: Implement access control mechanisms to determine what actions a client can perform on resources.
- HTTPS: Encrypt data in transit using HTTPS to protect it from eavesdropping.
- Input Validation: Validate and sanitize user inputs to prevent common security vulnerabilities like SQL injection and XSS attacks.
- Rate Limiting: Implement rate limiting to prevent abuse or overload of the API.
- OAuth Tokens: Use short-lived OAuth tokens to manage access and authorization.
- Audit Logs: Keep detailed logs of API access for monitoring and auditing purposes.
- Security Headers: Add security headers like Content Security Policy (CSP) and Cross-Origin Resource Policy (CORP) to protect against various attacks.

19. How do you rate limit access to a REST API?
- Decide on the rate limiting strategy you want to implement. 
- Common strategies include:
    - IP-Based Rate Limiting: Limit requests based on the IP address of the client. This approach is straightforward but can affect multiple users behind a shared IP (e.g., in a corporate network).
    - User-Based Rate Limiting: Limit requests based on user accounts or API keys. This strategy provides more fine-grained control and is often preferred for authenticated APIs.
    - Token Bucket Algorithm: Implement a token bucket algorithm that assigns tokens to clients, where each token represents a request. Clients can only make requests if they have tokens available. Tokens are replenished over time.

20. What is Cross-Origin Resource Sharing (CORS) in REST API security?
- Cross-Origin Resource Sharing (CORS) is a security feature that controls access to resources on a web page from different domains. 
- In the context of REST API security, CORS allows or restricts web applications running on one domain (the origin) to make requests to a different domain (another origin) to access API resources. 
- CORS policies are enforced by browsers and can be configured on the server hosting the REST API.
- Proper CORS configuration helps prevent unauthorized cross-origin requests and protects against potential security vulnerabilities. 
- CORS headers (e.g., Access-Control-Allow-Origin) specify which domains are allowed to access the API, what HTTP methods are permitted, and other security-related settings. 
- This mechanism ensures that only trusted domains can access the API's resources, reducing the risk of cross-site request forgery (CSRF) and other security threats.

21. How can you optimize performance in REST APIs?
- Optimizing performance in REST APIs involves several strategies:
    - Use Efficient Data Formats: Choose lightweight data formats like JSON over heavier formats like XML.
    - Pagination: Implement pagination to limit the amount of data returned in a single request.
    - Compression: Use data compression (e.g., gzip) to reduce the size of responses.
    - Caching: Implement server-side and client-side caching to reduce redundant requests.
    - CDNs: Use Content Delivery Networks (CDNs) to cache and serve static resources.
    - Optimized Queries: Optimize database queries to reduce response times.
    - Load Balancing: Distribute traffic across multiple servers to handle high loads.
    - Asynchronous Processing: Offload time-consuming tasks to background processes.
    - API Versioning: Carefully manage API versions to avoid breaking changes.
    - Minimize Round Trips: Reduce the number of HTTP requests needed to fulfill a client's request.

22. What's the role of caching in RESTful APIs?
- Caching plays a crucial role in RESTful APIs by improving performance, reducing server load, and enhancing the scalability of the API.
-  It is a fundamental tool for achieving fast and responsive API interactions while conserving server resources.

23. Are REST APIs suitable for mobile app development?
- Yes, REST APIs are suitable for mobile app development. 
- They are widely used in mobile app development due to their simplicity, scalability, and flexibility. Mobile apps can interact with RESTful services over standard HTTP, making it easy to consume data and perform actions from servers or other APIs. 
- Additionally, REST APIs work well with various programming languages and platforms, which is essential for cross-platform mobile development.

24. What's the difference between REST and GraphQL?
- REST (Representational State Transfer) 
    - It is an architectural style that uses a fixed set of endpoints (URLs) to access resources.
    - Clients typically receive a fixed structure of data in responses, which may lead to over-fetching or under-fetching of data.
- GraphQL 
    - It is a query language and runtime for APIs. 
    - It allows clients to specify exactly what data they need in a single request, eliminating over-fetching and under-fetching issues. 
    - GraphQL APIs have a single endpoint and offer a more flexible and efficient way to retrieve and manipulate data.

25. How do you document and test a REST API?
- Documentation: Create comprehensive API documentation that includes endpoints, request and response examples, authentication methods, and error handling.
- API Testing Tools: Use tools like Postman, Swagger, or Insomnia to manually test API endpoints by sending requests and verifying responses.
- Automated Testing: Implement automated testing using testing frameworks like Jest, PHPUnit, or Mocha to ensure that API endpoints work as expected.
- Load Testing: Conduct load testing to assess the API's performance and scalability under heavy traffic.
- Security Testing: Perform security testing to identify vulnerabilities such as SQL injection, XSS, and CSRF.
- Documentation Tools: Use API documentation tools like Swagger UI, Redoc, or ReDoc to generate interactive documentation from code comments or annotations.

26. What is backward compatibility in RESTful APIs?
- Backward compatibility in RESTful APIs refers to the ability of the API to accommodate changes and updates without breaking existing client applications. 
- When an API is backward compatible, existing clients can continue to use the API even after new features or modifications are introduced. 
- This ensures that clients built with the previous version of the API still function as expected without requiring immediate updates.

27. Can you give examples of common HTTP methods used in REST?
- Common HTTP methods used in REST include:
    - GET: Retrieve data from the server.
    - POST: Create a new resource on the server.
    - PUT: Update an existing resource on the server.
    - DELETE: Remove a resource from the server.
    - PATCH: Partially update a resource on the server.
    - HEAD: Retrieve metadata about a resource without the actual data.
    - OPTIONS: Determine the communication options available for a resource.

28. What are resources in a REST API?
- Resources in a REST API are the key abstractions that represent data or services. Resources can be tangible entities like user profiles, products, or articles, or they can represent services or actions like authentication or file uploads. 
- Each resource is identified by a unique URL (Uniform Resource Locator) and can be manipulated using standard HTTP methods.

29. What is CRUD in REST API operations?
- CRUD stands for Create, Read, Update, and Delete, which are the four fundamental operations that can be performed on resources in a REST API:
    - Create: Use the HTTP POST method to create a new resource on the server.
    - Read: Use the HTTP GET method to retrieve data or information about a resource.
    - Update: Use the HTTP PUT or PATCH method to modify an existing resource on the server.
    - Delete: Use the HTTP DELETE method to remove a resource from the server.
- These operations correspond to common database operations and are central to RESTful interactions with resources.

30. Why is JSON a popular format for data exchange in REST APIs?
- JSON (JavaScript Object Notation) is popular for data exchange in REST APIs for several reasons:
    - Human-Readable: JSON is easy for humans to read and write, which aids in debugging and development.
    - Lightweight: JSON has minimal overhead, making it efficient for data transmission.
    - Widely Supported: JSON is supported by most programming languages and platforms, making it accessible and versatile.
    - Structured: JSON provides a structured way to represent complex data, including nested objects and arrays.
    - Browser Compatibility: JSON can be easily parsed and manipulated in web browsers using JavaScript, making it suitable for web applications.
    - Standardized: JSON is a well-established data format with a clear specification, ensuring consistency in data representation.