document.addEventListener('DOMContentLoaded', () => {
  const article = document.querySelector('.md-content__inner');
  if (!article) return;

  const btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'article-copy-button';
  btn.setAttribute('aria-label', 'Copy full article');

  const ICON_DEFAULT = '⧉';
  const ICON_SUCCESS = '✓';
  const ICON_ERROR = '⚠';

  const setState = (icon, stateClass, label) => {
    btn.textContent = icon;
    btn.setAttribute('aria-label', label);
    btn.classList.remove('article-copy-button--success', 'article-copy-button--error');
    if (stateClass) btn.classList.add(stateClass);
  };

  setState(ICON_DEFAULT, null, 'Copy full article');

  const copyArticle = async () => {
    const clone = article.cloneNode(true);
    const copyBtn = clone.querySelector('.article-copy-button');
    if (copyBtn) copyBtn.remove();
    const text = (clone.innerText || '').trim();
    if (!text.trim()) return;
    try {
      await navigator.clipboard.writeText(text);
      setState(ICON_SUCCESS, 'article-copy-button--success', 'Copied full article');
      setTimeout(() => {
        setState(ICON_DEFAULT, null, 'Copy full article');
      }, 2000);
    } catch (err) {
      setState(ICON_ERROR, 'article-copy-button--error', 'Copy failed');
      setTimeout(() => {
        setState(ICON_DEFAULT, null, 'Copy full article');
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
