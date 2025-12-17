document.addEventListener('DOMContentLoaded', () => {
  const article = document.querySelector('.md-content__inner');
  if (!article) return;

  const btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'article-copy-button';
  btn.setAttribute('aria-label', 'Copy full article');
  btn.textContent = 'Copy article';

  const copyArticle = async () => {
    const text = article.innerText || '';
    if (!text.trim()) return;
    try {
      await navigator.clipboard.writeText(text);
      btn.textContent = 'Copied';
      btn.classList.add('article-copy-button--success');
      setTimeout(() => {
        btn.textContent = 'Copy article';
        btn.classList.remove('article-copy-button--success');
      }, 2000);
    } catch (err) {
      btn.textContent = 'Copy failed';
      btn.classList.add('article-copy-button--error');
      setTimeout(() => {
        btn.textContent = 'Copy article';
        btn.classList.remove('article-copy-button--error');
      }, 2000);
    }
  };

  btn.addEventListener('click', copyArticle);

  const firstHeading = article.querySelector('h1, h2, h3, h4, h5, h6');
  if (firstHeading && firstHeading.parentNode) {
    firstHeading.parentNode.insertBefore(btn, firstHeading);
  } else {
    article.prepend(btn);
  }
});
