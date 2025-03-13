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