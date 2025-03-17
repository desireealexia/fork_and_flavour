// Ingredients table in recipe_form.html
document.addEventListener("DOMContentLoaded", function () {
    const ingredientTableBody = document.querySelector("#ingredient-table tbody");
    const addIngredientBtn = document.getElementById("add-ingredient");
  
    if (ingredientTableBody && addIngredientBtn) {
      // Initialize SortableJS for the table
      let sortable = new Sortable(ingredientTableBody, {
        handle: ".drag-handle",
        animation: 150,
        onEnd: updateIngredientLabels,
      });
  
      function updateIngredientLabels() {
        const rows = document.querySelectorAll(".ingredient-item");
        rows.forEach((row, index) => {
          const label = row.querySelector(".ingredient-number");
          if (label) {
            label.textContent = `Ingredient ${index + 1}`;
          }
        });
      }
  
      // Add new ingredient row
      addIngredientBtn.addEventListener("click", function () {
        const newRow = document.createElement("tr");
        newRow.classList.add("ingredient-item");
        newRow.innerHTML = `
          <td class="drag-handle">☰</td>
          <td><input type="text" name="ingredient_name[]" placeholder="e.g. Chicken " class="form-control" required></td>
          <td><input type="number" name="ingredient_quantity[]" placeholder="e.g. 0.5, 250" step="0.5" class="form-control"></td>
          <td><input type="text" name="ingredient_unit[]" placeholder="e.g. g, ml" class="form-control"></td>
          <td class="text-center"><input type="checkbox" name="ingredient_optional[]" value="true" class="form-check-input"></td>
          <td class="text-center"><button type="button" class="btn btn-danger btn-sm remove-ingredient rounded-pill">✖</button></td>
        `;
        ingredientTableBody.appendChild(newRow);
  
        // Re-initialize SortableJS to include new rows
        sortable.destroy();
        sortable = new Sortable(ingredientTableBody, {
          handle: ".drag-handle",
          animation: 150,
          onEnd: updateIngredientLabels,
        });
  
        updateIngredientLabels();
      });
  
      // Remove ingredient row
      ingredientTableBody.addEventListener("click", function (e) {
        if (e.target.classList.contains("remove-ingredient")) {
          e.target.closest("tr").remove();
          updateIngredientLabels();
        }
      });
  
      updateIngredientLabels(); // Initialize numbering on page load
    }
  
    // Instructions in recipe_form.html
    const addStepBtn = document.getElementById("add-step-btn");
    const instructionInput = document.getElementById("instruction-step");
    const instructionsList = document.getElementById("instructions-list");
    const hiddenInput = document.getElementById("instructions-hidden-input");
  
    if (addStepBtn && instructionInput && instructionsList && hiddenInput) {
      let steps = [];
  
      function refreshList() {
        instructionsList.innerHTML = "";
        steps.forEach((step, index) => {
          const listItem = document.createElement("li");
          listItem.textContent = step;
  
          const deleteBtn = document.createElement("button");
          deleteBtn.textContent = "❌";
          deleteBtn.type = "button";
          deleteBtn.onclick = function () {
            steps.splice(index, 1);
            refreshList();
          };
  
          listItem.appendChild(deleteBtn);
          instructionsList.appendChild(listItem);
        });
  
        hiddenInput.value = steps.join("||");
      }
  
      addStepBtn.addEventListener("click", function () {
        const stepText = instructionInput.value.trim();
        if (stepText) {
          steps.push(stepText);
          refreshList();
          instructionInput.value = "";
        }
      });
    }
  });
  