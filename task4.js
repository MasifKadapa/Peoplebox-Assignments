function snakeToCamel(snakeObj) {
    let camelObj = {};
    for (let key in snakeObj) {
        if (snakeObj.hasOwnProperty(key)) {
            // Replace underscores and capitalize the next letter
            let camelKey = key.replace(/_([a-z])/g, (match, letter) => letter.toUpperCase());
            // Make the first letter lowercase to follow camelCase
            camelObj[camelKey[0].toLowerCase() + camelKey.slice(1)] = snakeObj[key];
        }
    }
    return camelObj;
}

// Example usage
const snakeCaseJson = {
    "first_name": "John",
    "last_name": "Doe",
    "email_address": "john.doe@example.com"
};

const camelCaseJson = snakeToCamel(snakeCaseJson);
console.log(camelCaseJson);
