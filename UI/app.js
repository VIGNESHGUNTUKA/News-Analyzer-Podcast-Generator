// UI State & Elements
let currentMode = 'manual';
let generatedPodcasts = [];
let bookmarkedPodcasts = JSON.parse(localStorage.getItem('newsPodBookmarks')) || [];
let currentPlayingFile = null;
let currentPlayingIndex = -1;

// Voice map matching config.py
const VOICES_MAP = {
    "English": [
        { name: "Female - Aria (Natural)", value: "en-US-AriaNeural" },
        { name: "Male - Christopher (Natural)", value: "en-US-ChristopherNeural" }
    ],
    "Telugu": [
        { name: "Female - Shruti (Natural)", value: "te-IN-ShrutiNeural" },
        { name: "Male - Mohan (Natural)", value: "te-IN-MohanNeural" }
    ],
    "Hindi": [
        { name: "Female - Swara (Natural)", value: "hi-IN-SwaraNeural" },
        { name: "Male - Madhur (Natural)", value: "hi-IN-MadhurNeural" }
    ],
    "Tamil": [
        { name: "Female - Pallavi (Natural)", value: "ta-IN-PallaviNeural" },
        { name: "Male - Valluvar (Natural)", value: "ta-IN-ValluvarNeural" }
    ]
};

document.addEventListener('DOMContentLoaded', () => {
    // Initialize Lucide Icons
    lucide.createIcons();

    // DOM Elements
    const navItems = document.querySelectorAll('.nav-item');
    const modeCards = document.querySelectorAll('.mode-card');
    const manualWorkspace = document.getElementById('manual-workspace');
    const automaticWorkspace = document.getElementById('automatic-workspace');
    const prefLanguage = document.getElementById('pref-language');
    const prefVoice = document.getElementById('pref-voice');
    const prefCategory = document.getElementById('pref-category');
    const categoryCards = document.querySelectorAll('.category-card');
    const prefCategoryWrapper = document.getElementById('pref-category-wrapper');
    const btnGenerate = document.getElementById('btn-generate');
    const newsTextarea = document.getElementById('news-textarea');
    const loadingOverlay = document.getElementById('loading-overlay');
    const loadingText = loadingOverlay.querySelector('h4');
    const loadingDesc = loadingOverlay.querySelector('p');

    // Audio Player Elements
    const audioEl = document.getElementById('html5-audio');
    const btnPlayPause = document.getElementById('player-play-pause');
    const playerTitle = document.getElementById('player-title');
    const playerStatus = document.getElementById('player-status');
    const progressTrack = document.getElementById('progress-track');
    const progressFill = document.getElementById('progress-fill');
    const progressThumb = document.getElementById('progress-thumb');
    const currentTimeEl = document.getElementById('player-current-time');
    const totalTimeEl = document.getElementById('player-total-time');
    const miniVisualizer = document.getElementById('player-mini-visualizer');
    const volumeTrack = document.getElementById('volume-track');
    const volumeFill = document.getElementById('volume-fill');
    const btnMute = document.getElementById('player-mute-btn');
    const favoriteBtn = document.querySelector('.favorite-btn');

    // 1. Navigation Tab Switching
    navItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            navItems.forEach(n => n.classList.remove('active'));
            item.classList.add('active');

            const tab = item.getAttribute('data-tab');
            
            // Clear active green border highlights from all sections and mode cards
            const welcomeBanner = document.querySelector('.welcome-banner');
            const bookEl = document.getElementById('bookmarks-section');
            const aboutEl = document.getElementById('about-us-section');
            if (welcomeBanner) welcomeBanner.classList.remove('active');
            if (bookEl) bookEl.classList.remove('active');
            if (aboutEl) aboutEl.classList.remove('active');

            if (tab === 'home') {
                document.querySelector('.page-container').classList.remove('hidden');
                document.querySelector('.page-container').scrollTo({ top: 0, behavior: 'smooth' });
                if (welcomeBanner) welcomeBanner.classList.add('active');
            } else if (tab === 'manual') {
                switchMode('manual');
            } else if (tab === 'automatic') {
                switchMode('automatic');
            } else if (tab === 'categories') {
                document.querySelector('.page-container').scrollTo({ top: 0, behavior: 'smooth' });
            } else if (tab === 'bookmarks') {
                if (bookEl) {
                    bookEl.classList.add('active');
                    bookEl.scrollIntoView({ behavior: 'smooth' });
                }
            } else if (tab === 'about') {
                if (aboutEl) {
                    aboutEl.classList.add('active');
                    aboutEl.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    });

    // 2. Mode Cards Switching
    modeCards.forEach(card => {
        card.addEventListener('click', () => {
            modeCards.forEach(c => c.classList.remove('active'));
            card.classList.add('active');

            const mode = card.getAttribute('data-mode');
            switchMode(mode);
        });
    });

    function switchMode(mode) {
        currentMode = mode;
        const welcomeBanner = document.querySelector('.welcome-banner');
        if (welcomeBanner) welcomeBanner.classList.remove('active');
        if (mode === 'manual') {
            manualWorkspace.classList.remove('hidden');
            automaticWorkspace.classList.add('hidden');
            if (prefCategoryWrapper) prefCategoryWrapper.style.display = 'none';
            document.querySelector('[data-mode="manual"]').classList.add('active');
            document.querySelector('[data-mode="automatic"]').classList.remove('active');
        } else {
            manualWorkspace.classList.add('hidden');
            automaticWorkspace.classList.remove('hidden');
            if (prefCategoryWrapper) prefCategoryWrapper.style.display = 'flex';
            document.querySelector('[data-mode="manual"]').classList.remove('active');
            document.querySelector('[data-mode="automatic"]').classList.add('active');
        }
        document.querySelector('.page-container').scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Category Card Selection & Dropdown Sync
    categoryCards.forEach(card => {
        card.addEventListener('click', () => {
            categoryCards.forEach(c => c.classList.remove('active'));
            card.classList.add('active');
            const selectedCat = card.getAttribute('data-category');
            if (prefCategory) {
                prefCategory.value = selectedCat;
            }
        });
    });

    if (prefCategory) {
        prefCategory.addEventListener('change', () => {
            const selectedCat = prefCategory.value;
            categoryCards.forEach(card => {
                if (card.getAttribute('data-category') === selectedCat) {
                    card.classList.add('active');
                } else {
                    card.classList.remove('active');
                }
            });
        });
    }

    // 3. Language & Voice Dropdown Integration
    prefLanguage.addEventListener('change', () => {
        const lang = prefLanguage.value;
        populateVoices(lang);
    });

    function populateVoices(language) {
        prefVoice.innerHTML = '';
        const voices = VOICES_MAP[language] || [];
        voices.forEach(voice => {
            const option = document.createElement('option');
            option.value = voice.value;
            option.textContent = voice.name;
            prefVoice.appendChild(option);
        });
    }

    // 4. Load Headlines
    async function loadHeadlines() {
        const container = document.getElementById('headlines-container');
        try {
            const res = await fetch('/api/headlines');
            const headlines = await res.json();

            if (headlines.length === 0) {
                container.innerHTML = '<div class="headline-skeleton">No headlines collected yet.</div>';
                return;
            }

            container.innerHTML = '';
            const top10Headlines = headlines.slice(0, 5);
            top10Headlines.forEach((art, index) => {
                const card = document.createElement('div');
                card.className = 'headline-card';
                card.innerHTML = `
                    <img class="headline-img" src="${art.image || 'https://images.unsplash.com/photo-1495020689067-958852a6565d?w=150'}" alt="News Image">
                    <div class="headline-content">
                        <div class="headline-meta">
                            <span class="headline-category">${art.category}</span>
                            <span>&bull;</span>
                            <span>${art.source}</span>
                            <span>&bull;</span>
                            <span>${art.publishedAt}</span>
                        </div>
                        <h4 class="headline-title">${art.title}</h4>
                    </div>
                `;
                // Autofill textarea when clicking headlines (for convenience in manual mode)
                card.addEventListener('click', () => {
                    if (currentMode === 'manual') {
                        newsTextarea.value = `${art.title}\n\n${art.description}`;
                        newsTextarea.focus();
                    }
                });
                container.appendChild(card);
            });
        } catch (e) {
            console.error(e);
            container.innerHTML = '<div class="headline-skeleton">Failed to load headlines.</div>';
        }
    }

    // 5. Load Podcasts
    async function loadPodcasts() {
        const container = document.getElementById('podcasts-container');
        try {
            const res = await fetch('/api/podcasts');
            generatedPodcasts = await res.json();

            if (generatedPodcasts.length === 0) {
                container.innerHTML = '<div class="podcast-skeleton">No podcasts generated yet. Set preferences and click Generate!</div>';
                return;
            }

            container.innerHTML = '';
            generatedPodcasts.forEach((pod) => {
                const isPlaying = currentPlayingFile === pod.filename;
                const isBookmarked = bookmarkedPodcasts.some(b => b.filename === pod.filename);
                const card = document.createElement('div');
                card.className = `podcast-card ${isPlaying ? 'playing' : ''}`;
                card.innerHTML = `
                    <div class="podcast-left">
                        <div class="podcast-play-btn" data-url="${pod.url}" data-filename="${pod.filename}">
                            <i data-lucide="${isPlaying && !audioEl.paused ? 'pause' : 'play'}"></i>
                        </div>
                        <div class="podcast-info">
                            <h4 class="podcast-title">${pod.category} News Podcast - ${pod.language}</h4>
                            <p class="podcast-meta">${pod.date}</p>
                        </div>
                    </div>
                    <div class="podcast-actions">
                        <a href="${pod.url}" download="${pod.filename}" class="podcast-action-btn" title="Download Audio">
                            <i data-lucide="download"></i>
                        </a>
                        <button class="podcast-action-btn favorite-podcast-btn ${isBookmarked ? 'active' : ''}" title="Bookmark">
                            <i data-lucide="bookmark"></i>
                        </button>
                    </div>
                `;

                // Click card play button
                const playBtn = card.querySelector('.podcast-play-btn');
                playBtn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    playPodcast(pod);
                });

                // Bookmark toggle handler
                const bookmarkBtn = card.querySelector('.favorite-podcast-btn');
                bookmarkBtn.addEventListener('click', (e) => {
                    e.stopPropagation();
                    toggleBookmark(pod);
                });

                container.appendChild(card);
            });
            lucide.createIcons();
            renderBookmarks();
        } catch (e) {
            console.error(e);
            container.innerHTML = '<div class="podcast-skeleton">Failed to load podcast library.</div>';
        }
    }

    // Toggle Bookmark Function
    function toggleBookmark(pod) {
        const index = bookmarkedPodcasts.findIndex(b => b.filename === pod.filename);
        if (index > -1) {
            bookmarkedPodcasts.splice(index, 1);
        } else {
            bookmarkedPodcasts.push(pod);
        }
        localStorage.setItem('newsPodBookmarks', JSON.stringify(bookmarkedPodcasts));
        loadPodcasts();
        renderBookmarks();
    }

    // Render Bookmarks Section Function
    function renderBookmarks() {
        const bContainer = document.getElementById('bookmarks-container');
        if (!bContainer) return;

        if (bookmarkedPodcasts.length === 0) {
            bContainer.innerHTML = '<div class="podcast-skeleton">No bookmarked podcasts yet. Click the bookmark icon on any podcast to save it!</div>';
            return;
        }

        bContainer.innerHTML = '';
        bookmarkedPodcasts.forEach((pod) => {
            const isPlaying = currentPlayingFile === pod.filename;
            const card = document.createElement('div');
            card.className = `podcast-card ${isPlaying ? 'playing' : ''}`;
            card.innerHTML = `
                <div class="podcast-left">
                    <div class="podcast-play-btn" data-url="${pod.url}" data-filename="${pod.filename}">
                        <i data-lucide="${isPlaying && !audioEl.paused ? 'pause' : 'play'}"></i>
                    </div>
                    <div class="podcast-info">
                        <h4 class="podcast-title">${pod.category} News Podcast - ${pod.language}</h4>
                        <p class="podcast-meta">${pod.date}</p>
                    </div>
                </div>
                <div class="podcast-actions">
                    <a href="${pod.url}" download="${pod.filename}" class="podcast-action-btn" title="Download Audio">
                        <i data-lucide="download"></i>
                    </a>
                    <button class="podcast-action-btn favorite-podcast-btn active" title="Remove Bookmark">
                        <i data-lucide="bookmark"></i>
                    </button>
                </div>
            `;

            const playBtn = card.querySelector('.podcast-play-btn');
            playBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                playPodcast(pod);
            });

            const bookmarkBtn = card.querySelector('.favorite-podcast-btn');
            bookmarkBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                toggleBookmark(pod);
            });

            bContainer.appendChild(card);
        });
        lucide.createIcons();
    }

    // Play Podcast Function
    function playPodcast(pod) {
        if (currentPlayingFile === pod.filename) {
            // Toggle pause/play
            if (audioEl.paused) {
                audioEl.play();
            } else {
                audioEl.pause();
            }
            return;
        }

        currentPlayingFile = pod.filename;
        currentPlayingIndex = generatedPodcasts.findIndex(p => p.filename === pod.filename);
        audioEl.src = pod.url;
        audioEl.load();
        audioEl.play();

        playerTitle.textContent = `${pod.category} News Podcast`;
        playerStatus.textContent = `${pod.language} Voice | Playing`;

        // Save state UI updates
        updatePodcastListUI();
    }

    function updatePodcastListUI() {
        document.querySelectorAll('.podcast-card').forEach(card => {
            const playBtn = card.querySelector('.podcast-play-btn');
            const file = playBtn.getAttribute('data-filename');
            const icon = playBtn.querySelector('i');

            if (file === currentPlayingFile) {
                card.classList.add('playing');
                if (audioEl.paused) {
                    playBtn.innerHTML = '<i data-lucide="play"></i>';
                } else {
                    playBtn.innerHTML = '<i data-lucide="pause"></i>';
                }
            } else {
                card.classList.remove('playing');
                playBtn.innerHTML = '<i data-lucide="play"></i>';
            }
        });
        lucide.createIcons();

        // Update Bottom Player Play Pause button
        if (audioEl.paused) {
            btnPlayPause.innerHTML = '<i data-lucide="play"></i>';
            miniVisualizer.classList.add('paused');
        } else {
            btnPlayPause.innerHTML = '<i data-lucide="pause"></i>';
            miniVisualizer.classList.remove('paused');
        }
        lucide.createIcons();
    }

    // 6. Generate Podcast Button Action
    btnGenerate.addEventListener('click', async () => {
        const language = prefLanguage.value;
        const selectedOpt = prefLanguage.options[prefLanguage.selectedIndex];
        const lang_code = selectedOpt.getAttribute('data-code');
        const selectedCategory = prefCategory ? prefCategory.value : 'General';
        const category = currentMode === 'automatic' ? selectedCategory : 'General';
        const voice = prefVoice.value;

        let bodyData = { language, lang_code, category, voice };
        let url = '';

        if (currentMode === 'manual') {
            const text = newsTextarea.value.trim();
            if (!text) {
                alert("Please paste some news article text first!");
                return;
            }
            bodyData.text = text;
            url = '/api/generate/manual';
            loadingText.textContent = "Analyzing Article...";
            loadingDesc.textContent = "Running word frequency algorithms, category detector, and generating podcast script...";
        } else {
            url = '/api/generate/automatic';
            loadingText.textContent = `Collecting ${category} News...`;
            loadingDesc.textContent = `Fetching ${category} news updates from global headlines database, summarizing content, and rendering audio...`;
        }

        // Show overlay
        loadingOverlay.classList.remove('hidden');

        try {
            const res = await fetch(url, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(bodyData)
            });
            const data = await res.json();

            if (data.success) {
                // Success! Reload Podcasts
                await loadPodcasts();

                // Clear textarea if manual
                if (currentMode === 'manual') {
                    newsTextarea.value = '';
                }

                // Play the newly generated podcast (it should be the first one in the list)
                if (generatedPodcasts.length > 0) {
                    playPodcast(generatedPodcasts[0]);
                }
            } else {
                alert(`Error: ${data.error || 'Failed to generate podcast'}`);
            }
        } catch (e) {
            console.error(e);
            alert("Connection error while communicating with generator service.");
        } finally {
            loadingOverlay.classList.add('hidden');
        }
    });

    // 7. Bottom Player Custom Handles
    btnPlayPause.addEventListener('click', () => {
        if (!audioEl.src) return;
        if (audioEl.paused) {
            audioEl.play();
        } else {
            audioEl.pause();
        }
    });

    audioEl.addEventListener('play', () => {
        updatePodcastListUI();
    });

    audioEl.addEventListener('pause', () => {
        updatePodcastListUI();
    });

    audioEl.addEventListener('timeupdate', () => {
        const cur = audioEl.currentTime;
        const dur = audioEl.duration || 0;

        // Calculate progress percentage
        const percent = dur > 0 ? (cur / dur) * 100 : 0;
        progressFill.style.width = `${percent}%`;
        progressThumb.style.left = `${percent}%`;

        // Formatted times
        currentTimeEl.textContent = formatTime(cur);
        totalTimeEl.textContent = formatTime(dur);
    });

    function formatTime(secs) {
        if (isNaN(secs)) return "00:00";
        const m = Math.floor(secs / 60).toString().padStart(2, '0');
        const s = Math.floor(secs % 60).toString().padStart(2, '0');
        return `${m}:${s}`;
    }

    // Seek interaction
    progressTrack.addEventListener('click', (e) => {
        if (!audioEl.src || audioEl.duration === 0) return;
        const rect = progressTrack.getBoundingClientRect();
        const clickX = e.clientX - rect.left;
        const width = rect.width;
        const percentage = clickX / width;
        audioEl.currentTime = percentage * audioEl.duration;
    });

    // Volume controls
    volumeTrack.addEventListener('click', (e) => {
        const rect = volumeTrack.getBoundingClientRect();
        const clickX = e.clientX - rect.left;
        const width = rect.width;
        let percentage = clickX / width;
        if (percentage < 0) percentage = 0;
        if (percentage > 1) percentage = 1;

        audioEl.volume = percentage;
        volumeFill.style.width = `${percentage * 100}%`;

        if (percentage === 0) {
            btnMute.innerHTML = '<i data-lucide="volume-x"></i>';
        } else if (percentage < 0.5) {
            btnMute.innerHTML = '<i data-lucide="volume-1"></i>';
        } else {
            btnMute.innerHTML = '<i data-lucide="volume-2"></i>';
        }
        lucide.createIcons();
    });

    btnMute.addEventListener('click', () => {
        audioEl.muted = !audioEl.muted;
        if (audioEl.muted) {
            btnMute.innerHTML = '<i data-lucide="volume-x"></i>';
            volumeFill.style.width = '0%';
        } else {
            btnMute.innerHTML = '<i data-lucide="volume-2"></i>';
            volumeFill.style.width = `${audioEl.volume * 100}%`;
        }
        lucide.createIcons();
    });

    // Previous & Next podcast navigation
    const btnPrev = document.getElementById('player-prev');
    const btnNext = document.getElementById('player-next');

    btnPrev.addEventListener('click', () => {
        if (generatedPodcasts.length === 0) return;
        let prevIndex = currentPlayingIndex - 1;
        if (prevIndex < 0) prevIndex = generatedPodcasts.length - 1;
        playPodcast(generatedPodcasts[prevIndex]);
    });

    btnNext.addEventListener('click', () => {
        if (generatedPodcasts.length === 0) return;
        let nextIndex = currentPlayingIndex + 1;
        if (nextIndex >= generatedPodcasts.length) nextIndex = 0;
        playPodcast(generatedPodcasts[nextIndex]);
    });

    // Auto-advance to next podcast when current one ends
    audioEl.addEventListener('ended', () => {
        if (generatedPodcasts.length === 0) return;
        let nextIndex = currentPlayingIndex + 1;
        if (nextIndex < generatedPodcasts.length) {
            playPodcast(generatedPodcasts[nextIndex]);
        } else {
            // End of playlist
            playerStatus.textContent = 'Playlist ended';
            miniVisualizer.classList.add('paused');
            btnPlayPause.innerHTML = '<i data-lucide="play"></i>';
            lucide.createIcons();
        }
    });

    // Bottom action clicks
    favoriteBtn.addEventListener('click', () => favoriteBtn.classList.toggle('active'));



    // Global Search Functionality
    const searchInput = document.getElementById('main-search-input');
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            const term = e.target.value.trim().toLowerCase();

            // Filter Headlines
            const headlineCards = document.querySelectorAll('.headline-card');
            let headlineMatchCount = 0;
            headlineCards.forEach(card => {
                const text = card.textContent.toLowerCase();
                if (term === '' || text.includes(term)) {
                    card.style.display = 'flex';
                    headlineMatchCount++;
                } else {
                    card.style.display = 'none';
                }
            });

            // Filter Podcasts (in recent podcasts and bookmarks)
            const podcastCards = document.querySelectorAll('.podcast-card');
            let podcastMatchCount = 0;
            podcastCards.forEach(card => {
                const text = card.textContent.toLowerCase();
                if (term === '' || text.includes(term)) {
                    card.style.display = 'flex';
                    podcastMatchCount++;
                } else {
                    card.style.display = 'none';
                }
            });

            // If user typed something, smoothly scroll to feed grid so results are immediately visible
            if (term.length === 1) {
                const feedGrid = document.querySelector('.feed-grid');
                if (feedGrid) {
                    feedGrid.scrollIntoView({ behavior: 'smooth' });
                }
            }
        });
    }

    // Startup Init
    const welcomeBanner = document.querySelector('.welcome-banner');
    if (welcomeBanner) welcomeBanner.classList.add('active');
    populateVoices("Telugu");
    switchMode('manual');
    loadHeadlines();
    loadPodcasts();
});
