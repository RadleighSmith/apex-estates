document.addEventListener('DOMContentLoaded', function() {
    const propertyTitles = document.querySelectorAll('.card-title');

    propertyTitles.forEach(title => {
        let titleText = title.textContent;
        const maxTitleLength = 120;

        if (titleText.length > maxTitleLength) {
            title.textContent = titleText.slice(0, maxTitleLength) + '...';
        }
    });
});