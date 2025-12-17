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
    // Clone content and remove copy buttons from the clone
    const clone = article.cloneNode(true);
    clone.querySelectorAll('.article-copy-button').forEach((el) => el.remove());
    const text = (clone.innerText || '').trim();
    if (!text) return;
    try {
      await navigator.clipboard.writeText(text);
      setState(ICON_SUCCESS, 'article-copy-button--success', 'Copied full article');
      setTimeout(() => setState(ICON_DEFAULT, null, 'Copy full article'), 1800);
    } catch (err) {
      setState(ICON_ERROR, 'article-copy-button--error', 'Copy failed');
      setTimeout(() => setState(ICON_DEFAULT, null, 'Copy full article'), 1800);
    }
  };

  btn.addEventListener('click', copyArticle);

  // Place button at very top of article to avoid being copied from live DOM
  article.insertBefore(btn, article.firstChild);
});
