// Ingredients table in recipe_form.html
document.addEventListener('DOMContentLoaded', function () {
    const ingredientTableBody = document.querySelector('#ingredient-table tbody');
    const addIngredientBtn = document.getElementById('add-ingredient');

    // Initialize SortableJS for the table
    let sortable = new Sortable(ingredientTableBody, {
        handle: '.drag-handle',
        animation: 150,
        onEnd: updateIngredientLabels
    });

    // Function to update numbering (if needed)
    function updateIngredientLabels() {
        const rows = document.querySelectorAll('.ingredient-item');
        rows.forEach((row, index) => {
            const label = row.querySelector('.ingredient-number');
            if (label) {
                label.textContent = `Ingredient ${index + 1}`;
            }
        });
    }

    // Add new ingredient row
    addIngredientBtn.addEventListener('click', function () {
        const newRow = document.createElement('tr');
        newRow.classList.add('ingredient-item');
        newRow.innerHTML = `
            <td class="drag-handle text-center">☰</td>
            <td><input type="text" name="ingredient_name[]" class="form-control" required></td>
            <td><input type="number" name="ingredient_quantity[]" step="0.01" class="form-control"></td>
            <td><input type="text" name="ingredient_unit[]" class="form-control"></td>
            <td class="text-center">
                <input type="checkbox" name="ingredient_optional[]" value="true">
            </td>
            <td class="text-center">
                <button type="button" class="btn btn-danger btn-sm remove-ingredient">Remove</button>
            </td>
        `;
        ingredientTableBody.appendChild(newRow);

        // Re-initialize SortableJS to include new rows
        sortable.destroy();
        sortable = new Sortable(ingredientTableBody, {
            handle: '.drag-handle',
            animation: 150,
            onEnd: updateIngredientLabels
        });

        updateIngredientLabels();
    });

    // Remove ingredient row
    ingredientTableBody.addEventListener('click', function (e) {
        if (e.target.classList.contains('remove-ingredient')) {
            e.target.closest('tr').remove();
            updateIngredientLabels();  // Update numbering
        }
    });

    updateIngredientLabels(); // Initialize numbering on page load
});

// Instructions in recipe_form.html
document.addEventListener('DOMContentLoaded', function () {
    const addStepBtn = document.getElementById('add-step-btn');
    const instructionInput = document.getElementById('instruction-step');
    const instructionsList = document.getElementById('instructions-list');
    const hiddenInput = document.getElementById('instructions-hidden-input');

    let steps = [];

    // Function to refresh the list and maintain order
    function refreshList() {
        instructionsList.innerHTML = ''; // Clear current list
        steps.forEach((step, index) => {
            const listItem = document.createElement('li');
            listItem.textContent = step;

            // Add delete button
            const deleteBtn = document.createElement('button');
            deleteBtn.textContent = '❌';
            deleteBtn.type = 'button';
            deleteBtn.onclick = function () {
                steps.splice(index, 1); // Remove step from array
                refreshList();  // Refresh to maintain numbering
            };

            listItem.appendChild(deleteBtn);
            instructionsList.appendChild(listItem);
        });

        // Update hidden input with '||' separator
        hiddenInput.value = steps.join('||');
    }

    // Add Step Button Click
    addStepBtn.addEventListener('click', function () {
        const stepText = instructionInput.value.trim();
        if (stepText) {
            steps.push(stepText);
            refreshList(); // Refresh the list to include the new step
            instructionInput.value = ''; // Clear input after adding
        }
    });
});
