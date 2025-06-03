$(document).ready(function() {
    $('.toggleText').click(function(e) {
        e.preventDefault();
        
        var $this = $(this);
        var $content = $this.prev(".text-content");
        
        if ($content.hasClass('truncate')) {
            $content.removeClass('truncate');
            $this.text('Leer menos');
        } else {
            $content.addClass('truncate');
            $this.text('Leer más');
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    let modals = document.querySelectorAll('.modal');
    modals.forEach(function(modal) {
      new mdb.Modal(modal);
    });
  });