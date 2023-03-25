$(document).ready(function () {
  const searchInput = $('.w-100.rounded');
  const listItems = $('.list-group .list-group-item');

  searchInput.autocomplete({
    source: function (request, response) {
      const matcher = new RegExp($.ui.autocomplete.escapeRegex(request.term), 'i');
      response(listItems.map(function () {
        const trainingText = $(this).find('#training').text();
        if (matcher.test(trainingText)) {
          return trainingText;
        }
      }).get());
    },
    minLength: 1,
    select: function (event, ui) {
      searchInput.val(ui.item.value);
      filterListItems(ui.item.value);
      return false;
    },
  });

  searchInput.on('input', function () {
    filterListItems($(this).val());
  });

  function filterListItems(searchValue) {
    searchValue = searchValue.toLowerCase();
    listItems.filter(function () {
      $(this).toggle($(this).find('#training').text().toLowerCase().indexOf(searchValue) > -1);
    });
  }
});
