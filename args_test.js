module.exports = {
    // This function expects an object/dictionary
    verify_data: (data) => {
        console.log("--- JS SIDE LOGS ---");
        console.log("JS received data type:", typeof data);
        console.log("JS received content:", JSON.stringify(data));
        
        // Let's verify it's a real object
        if (data.skills && Array.isArray(data.skills)) {
             return "Success: JS received the array inside the dict!";
        }
        return "Failure: Data structure lost.";
    }
};