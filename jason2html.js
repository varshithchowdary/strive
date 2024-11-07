export default function json2html(data) {
    // Start with the opening table tag and add the data-user attribute
    let html = '<table data-user="varshithlion@gmail.com">';
    
    // Add the table header
    html += '<thead><tr><th>Name</th><th>Age</th><th>Gender</th></tr></thead>';
    
    // Add the table body
    html += '<tbody>';
    
    // Loop through each object in the data array
    data.forEach(item => {
        html += '<tr>';
        html += `<td>${item.Name}</td>`;
        html += `<td>${item.Age}</td>`;
        // Check if the Gender property exists, otherwise leave it empty
        html += `<td>${item.Gender || ''}</td>`;
        html += '</tr>';
    });

    // Close the table tag
    html += '</tbody></table>';

    // Return the generated HTML string
    return html;
}
