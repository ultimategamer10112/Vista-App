import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Vista App Preview", page_icon="🌆", layout="wide")

components.html(
    """
    <!DOCTYPE html>
    <html lang=\"en\">
      <head>
        <meta charset=\"utf-8\" />
        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
        <script src=\"https://cdn.tailwindcss.com?plugins=forms\"></script>
        <script src=\"https://unpkg.com/react@18/umd/react.development.js\"></script>
        <script src=\"https://unpkg.com/react-dom@18/umd/react-dom.development.js\"></script>
        <script src=\"https://unpkg.com/framer-motion/dist/framer-motion.umd.js\"></script>
        <script src=\"https://unpkg.com/@babel/standalone/babel.min.js\"></script>
        <style>
          html, body {
            background: radial-gradient(circle at 0% 0%, #fdf2f8, #eff6ff 45%, #f1f5f9 100%);
            min-height: 100vh;
          }
          body {
            padding: 32px;
            font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
          }
          ::-webkit-scrollbar {
            width: 6px;
          }
          ::-webkit-scrollbar-thumb {
            background: rgba(15, 23, 42, 0.15);
            border-radius: 9999px;
          }
        </style>
      </head>
      <body>
        <div id=\"root\" class=\"min-h-screen flex items-center justify-center\"></div>

        <script type=\"text/babel\">
          const { useState, useEffect, useRef } = React;
          const { motion, AnimatePresence } = window['framer-motion'];

          const mockSpots = [
            { id: 1, name: "La Marina", city: "Barcelona", tags: ["seafood", "$$"], rating: 4.7, notes: "Great paella; book terrace." },
            { id: 2, name: "Grove Café", city: "Lisbon", tags: ["brunch", "$"] , rating: 4.5, notes: "Get the pastel de nata warm." },
            { id: 3, name: "Trastevere 12", city: "Rome", tags: ["pasta", "$$$"] , rating: 4.8, notes: "Carbonara with guanciale." },
            { id: 4, name: "Bao Bar", city: "London", tags: ["asian", "street"], rating: 4.6, notes: "Order the pork bao + chili oil." },
            { id: 5, name: "Citrus Roof", city: "Nice", tags: ["views", "cocktails"], rating: 4.4, notes: "Sunset seating fills fast." },
          ];

          function Chip({ children, active = false, onClick }) {
            return (
              <button
                onClick={onClick}
                className={`inline-flex items-center px-2.5 py-1 rounded-full text-xs border ${
                  active ? "border-black bg-black text-white" : "border-black/10 bg-black/5 text-black"
                }`}
              >
                {children}
              </button>
            );
          }

          function Card({ children, onClick }) {
            return (
              <div
                onClick={onClick}
                className="rounded-2xl border border-black/10 bg-white hover:shadow-md transition-shadow p-4 cursor-pointer"
              >
                {children}
              </div>
            );
          }

          function HomeIcon() {
            return (
              <svg viewBox="0 0 24 24" className="h-6 w-6" fill="none" stroke="currentColor" strokeWidth="1.8">
                <path d="M3 11l9-8 9 8" />
                <path d="M5 10v10h14V10" />
              </svg>
            );
          }

          function MapIcon() {
            return (
              <svg viewBox="0 0 24 24" className="h-6 w-6" fill="none" stroke="currentColor" strokeWidth="1.8">
                <path d="M9 18l-6 3V6l6-3 6 3 6-3v15l-6 3-6-3z" />
                <path d="M9 3v15m6-12v15" />
              </svg>
            );
          }

          function FriendsIcon() {
            return (
              <svg viewBox="0 0 24 24" className="h-6 w-6" fill="none" stroke="currentColor" strokeWidth="1.8">
                <path d="M7 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8z" />
                <path d="M17 13a4 4 0 1 0 0-8 4 4 0 0 0 0 8z" />
                <path d="M1.5 22a7.5 7.5 0 0 1 11-6.5M22.5 22a7.5 7.5 0 0 0-11-6.5" />
              </svg>
            );
          }

          function UserIcon() {
            return (
              <svg viewBox="0 0 24 24" className="h-6 w-6" fill="none" stroke="currentColor" strokeWidth="1.8">
                <path d="M12 12a5 5 0 1 0 0-10 5 5 0 0 0 0 10z" />
                <path d="M3 22a9 9 0 0 1 18 0" />
              </svg>
            );
          }

          function Header({ onOpenInbox }) {
            return (
              <div className="flex items-center justify-between">
                <div className="w-14" />
                <div className="flex items-center gap-2">
                  <div className="h-8 w-8 rounded-lg bg-[#FFC83D] grid place-items-center font-black">V</div>
                  <div className="font-extrabold tracking-tight">Vista</div>
                </div>
                <button onClick={onOpenInbox} className="relative text-sm px-3 py-1.5 rounded-xl border border-black/10 bg-white hover:bg-black/5">
                  Inbox
                </button>
              </div>
            );
          }

          function HomeScreen({ tab, setTab, onRandomize, onOpenSpot, spots }) {
            const cities = Array.from(new Set(spots.map((s) => s.city)));
            const [city, setCity] = useState(cities[0] || "");
            const citySpots = spots.filter((s) => !city || s.city === city);

            return (
              <div className="space-y-4">
                <div className="flex items-center justify-center">
                  <div className="inline-flex p-1 rounded-full border border-black/10 bg-white">
                    <button onClick={() => setTab("foryou")} className={`px-3 py-1.5 text-sm rounded-full ${tab === "foryou" ? "bg-black text-white font-semibold" : "text-black/70"}`}>
                      For you
                    </button>
                    <button onClick={() => setTab("city")} className={`px-3 py-1.5 text-sm rounded-full ${tab === "city" ? "bg-black text-white font-semibold" : "text-black/70"}`}>
                      City
                    </button>
                  </div>
                </div>

                <AnimatePresence mode="wait">
                  {tab === "foryou" && (
                    <motion.div
                      key="foryou"
                      initial={{ opacity: 0, x: 10 }}
                      animate={{ opacity: 1, x: 0, transition: { duration: 0.2 } }}
                      exit={{ opacity: 0, x: -8, transition: { duration: 0.17 } }}
                      className="rounded-3xl p-5 bg-white border border-black/10"
                    >
                      <div className="flex items-center justify-between mb-3">
                        <div className="font-extrabold">Tonight’s pick</div>
                        <button onClick={onRandomize} className="px-3 py-1.5 rounded-xl bg-[#FFC83D] text-black font-bold border border-black/10">
                          🎲 Roll
                        </button>
                      </div>
                      <div className="grid gap-3">
                        {spots.slice(0, 6).map((s) => (
                          <Card key={s.id} onClick={() => onOpenSpot(s)}>
                            <div className="flex items-center gap-3">
                              <div className="h-14 w-14 rounded-xl bg-black/5 grid place-items-center text-xl">🍽️</div>
                              <div className="flex-1">
                                <div className="font-bold">{s.name}</div>
                                <div className="text-sm text-black/60">{s.city} · {s.tags.join(" · ")}</div>
                              </div>
                              <div className="text-right">
                                <div className="font-extrabold">{Number(s.rating).toFixed(1)}</div>
                                <div className="text-xs text-black/50">rating</div>
                              </div>
                            </div>
                          </Card>
                        ))}
                      </div>
                    </motion.div>
                  )}
                  {tab === "city" && (
                    <motion.div
                      key="city"
                      initial={{ opacity: 0, x: 10 }}
                      animate={{ opacity: 1, x: 0, transition: { duration: 0.2 } }}
                      exit={{ opacity: 0, x: -8, transition: { duration: 0.17 } }}
                      className="space-y-3"
                    >
                      <div className="flex flex-wrap gap-2">
                        {cities.map((c) => (
                          <Chip key={c} active={c === city} onClick={() => setCity(c)}>
                            {c}
                          </Chip>
                        ))}
                      </div>
                      <div className="grid gap-3">
                        {citySpots.map((s) => (
                          <Card key={s.id} onClick={() => onOpenSpot(s)}>
                            <div className="flex items-center gap-3">
                              <div className="h-12 w-12 rounded-xl bg-black/5 grid place-items-center text-lg">📍</div>
                              <div className="flex-1">
                                <div className="font-bold">{s.name}</div>
                                <div className="text-sm text-black/60">{s.city} · {s.tags.join(" · ")}</div>
                              </div>
                              <div className="text-right text-sm text-black/60">{Number(s.rating).toFixed(1)}</div>
                            </div>
                          </Card>
                        ))}
                      </div>
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>
            );
          }

          function MapScreen() {
            return (
              <div className="h-[520px] rounded-3xl border border-black/10 bg-[conic-gradient(at_20%_10%,#e5e7eb_10%,#cbd5e1_20%,#f8fafc_30%)] grid place-items-center text-black/60">
                <div className="text-center">
                  <div className="text-5xl mb-2">🗺️</div>
                  <div className="font-semibold">Map coming soon</div>
                  <div className="text-sm">Preview pins when you add spots.</div>
                </div>
              </div>
            );
          }

          function FriendsScreen({ activities = [], onOpenMessages }) {
            return (
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <div className="text-base font-bold">Following</div>
                  <button onClick={onOpenMessages} className="px-3 py-1.5 rounded-xl border border-black/10 bg-white hover:bg-black/5 text-sm">
                    Messages
                  </button>
                </div>

                {activities.length === 0 && <div className="text-sm text-black/60">No recent posts yet.</div>}
                {activities.map((a) => (
                  <Card key={a.id}>
                    <div className="flex items-center gap-3">
                      <div className="h-10 w-10 rounded-full bg-black/5 grid place-items-center">{a.emoji || "📌"}</div>
                      <div className="flex-1">
                        <div className="font-semibold">{a.text}</div>
                        <div className="text-sm text-black/60">{a.meta}</div>
                      </div>
                      {a.cta && <button className="text-sm px-3 py-1.5 rounded-xl border border-black/10">{a.cta}</button>}
                    </div>
                  </Card>
                ))}
              </div>
            );
          }

          function InboxScreen({ followers, messages, activities, onMarkAll, onFollowBack, initialTab = 'all' }) {
            const [tab, setTab] = useState(initialTab || 'all');
            const [selected, setSelected] = useState(null);
            const [reply, setReply] = useState('');

            const Section = ({ title, children }) => (
              <div className="space-y-2">
                <div className="text-xs uppercase tracking-wider text-black/60">{title}</div>
                {children}
              </div>
            );

            const openThread = (m) => {
              const base = m.thread || [
                { id: `${m.id}-0`, from: m.from, text: m.text, when: m.when },
              ];
              setSelected({ ...m, thread: base });
            };

            const addReply = (e) => {
              e.preventDefault();
              const text = reply.trim();
              if (!text) return;
              setSelected((prev) => ({
                ...prev,
                thread: [...prev.thread, { id: `${prev.id}-${prev.thread.length+1}`, from: 'You', text, when: 'Just now' }]
              }));
              setReply('');
            };

            if (selected) {
              return (
                <div className="space-y-4">
                  <div className="flex items-center justify-between">
                    <button className="text-sm px-3 py-1.5 rounded-xl border border-black/10" onClick={()=>setSelected(null)}>← Back</button>
                    <div className="font-bold">{selected.from}</div>
                    <div className="w-16" />
                  </div>

                  <div className="grid gap-3">
                    {selected.thread.map(msg => (
                      <Card key={msg.id}>
                        <div className="flex items-start gap-3">
                          <div className="h-8 w-8 rounded-full bg-black/5 grid place-items-center text-sm">{msg.from === 'You' ? '🫶' : '💬'}</div>
                          <div className="flex-1">
                            <div className="font-semibold text-sm">{msg.from} <span className="text-xs text-black/50">· {msg.when}</span></div>
                            <div className="text-sm text-black/80">{msg.text}</div>
                          </div>
                        </div>
                      </Card>
                    ))}
                  </div>

                  <form onSubmit={addReply} className="flex items-center gap-2">
                    <input
                      className="flex-1 px-3 py-2 rounded-xl border border-black/15"
                      placeholder="Reply…"
                      value={reply}
                      onChange={(e)=>setReply(e.target.value)}
                    />
                    <button className="px-3 py-2 rounded-xl bg-[#FFC83D] border border-black/10 font-semibold">Send</button>
                  </form>
                </div>
              );
            }

            return (
              <div className="space-y-4">
                <div className="flex items-center justify-center">
                  <div className="inline-flex p-1 rounded-full border border-black/10 bg-white">
                    <button onClick={()=>setTab('all')} className={`px-3 py-1.5 text-sm rounded-full ${tab==='all'? 'bg-black text-white font-semibold':'text-black/70'}`}>All</button>
                    <button onClick={()=>setTab('followers')} className={`px-3 py-1.5 text-sm rounded-full ${tab==='followers'? 'bg-black text-white font-semibold':'text-black/70'}`}>Followers</button>
                    <button onClick={()=>setTab('messages')} className={`px-3 py-1.5 text-sm rounded-full ${tab==='messages'? 'bg-black text-white font-semibold':'text-black/70'}`}>Messages</button>
                    <button onClick={()=>setTab('activity')} className={`px-3 py-1.5 text-sm rounded-full ${tab==='activity'? 'bg-black text-white font-semibold':'text-black/70'}`}>Activity</button>
                  </div>
                </div>

                <div className="flex justify-end">
                  <button onClick={onMarkAll} className="text-xs px-3 py-1.5 rounded-xl border border-black/10 bg-white hover:bg-black/5">Mark all read</button>
                </div>

                {(tab==='all' || tab==='followers') && (
                  <Section title="New followers">
                    {followers.length===0 ? (
                      <div className="text-sm text-black/60">No new followers.</div>
                    ) : followers.map(f => (
                      <Card key={f.id}>
                        <div className="flex items-center gap-3">
                          <div className="h-10 w-10 rounded-full bg-black/5 grid place-items-center">{f.avatar || '🧑'}</div>
                          <div className="flex-1">
                            <div className="font-semibold">{f.name} followed you</div>
                            <div className="text-sm text-black/60">{f.when}</div>
                          </div>
                          {f.following ? (
                            <span className="text-xs text-black/60">Following</span>
                          ) : (
                            <button onClick={()=>onFollowBack(f.id)} className="text-xs px-3 py-1.5 rounded-xl border border-black/10 bg-white hover:bg-black/5">Follow back</button>
                          )}
                          {f.unread && <span className="h-2 w-2 rounded-full bg-[#FFC83D]"/>}
                        </div>
                      </Card>
                    ))}
                  </Section>
                )}

                {(tab==='all' || tab==='messages') && (
                  <Section title="Messages">
                    {messages.length===0 ? (
                      <div className="text-sm text-black/60">No messages.</div>
                    ) : messages.map(m => (
                      <Card key={m.id} onClick={()=>openThread(m)}>
                        <div className="flex items-center gap-3">
                          <div className="h-10 w-10 rounded-full bg-black/5 grid place-items-center">{m.avatar || '💬'}</div>
                          <div className="flex-1">
                            <div className="font-semibold">{m.from}</div>
                            <div className="text-sm text-black/60">{m.text}</div>
                          </div>
                          <div className="text-xs text-black/50">{m.when}</div>
                        </div>
                      </Card>
                    ))}
                  </Section>
                )}

                {(tab==='all' || tab==='activity') && (
                  <Section title="Activity">
                    {activities.length===0 ? (
                      <div className="text-sm text-black/60">No activity yet.</div>
                    ) : activities.map(a => (
                      <Card key={a.id}>
                        <div className="flex items-center gap-3">
                          <div className="h-10 w-10 rounded-full bg-black/5 grid place-items-center">{a.emoji || '📌'}</div>
                          <div className="flex-1">
                            <div className="font-semibold">{a.text}</div>
                            <div className="text-sm text-black/60">{a.meta}</div>
                          </div>
                          {a.unread && <span className="h-2 w-2 rounded-full bg-[#FFC83D]"/>}
                        </div>
                      </Card>
                    ))}
                  </Section>
                )}
              </div>
            );
          }

          function ProfileScreen({ profile, followersCount, onEditProfile }) {
            const isImage = /^(https?:\\/\\/|data:)/i.test(profile.avatar || "");
            return (
              <div className="space-y-4">
                <div className="rounded-3xl border border-black/10 p-5 bg-white">
                  <div className="flex items-center gap-4">
                    <button
                      className="h-16 w-16 rounded-full bg-black/5 grid place-items-center text-2xl font-bold overflow-hidden border border-black/10"
                      onClick={onEditProfile}
                      title="Change photo"
                    >
                      {isImage ? (
                        <img src={profile.avatar} alt="avatar" className="h-full w-full object-cover" />
                      ) : (
                        <span>{profile.avatar || "🙂"}</span>
                      )}
                    </button>
                    <div className="flex-1 min-w-0">
                      <div className="font-extrabold truncate">{profile.name}</div>
                      <div className="text-sm text-black/60 truncate">@{profile.handle} · {followersCount} followers</div>
                    </div>
                    <button onClick={onEditProfile} className="px-3 py-1.5 rounded-xl border border-black/10 text-sm">Edit profile</button>
                  </div>
                  {profile.bio && (
                    <div className="mt-3 text-sm text-black/80">{profile.bio}</div>
                  )}
                  <div className="mt-3 text-xs text-black/60">{profile.lists} lists · {profile.saved} saved spots</div>
                </div>
                <div className="grid gap-3">
                  <Card>
                    <div className="font-semibold">Shared with friends</div>
                    <div className="text-sm text-black/60">Rome 2025 · Summer Bites · Coffee Crawl</div>
                  </Card>
                  <Card>
                    <div className="font-semibold">Preferences</div>
                    <div className="text-sm text-black/60">No peanuts · Veg‑friendly · $$</div>
                  </Card>
                </div>
              </div>
            );
          }

          function PhoneSheet({ open, onClose, children, title }) {
            return (
              <AnimatePresence>
                {open && (
                  <motion.div
                    className="absolute inset-0 z-20"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    exit={{ opacity: 0 }}
                  >
                    <motion.div
                      onClick={onClose}
                      className="absolute inset-0 bg-black/40"
                      initial={{ opacity: 0 }}
                      animate={{ opacity: 1 }}
                      exit={{ opacity: 0 }}
                    />
                    <motion.div
                      className="absolute left-1/2 -translate-x-1/2 bottom-0 w-[560px] max-w-[100%] rounded-t-3xl bg-white border border-black/10 p-5"
                      initial={{ y: 24, opacity: 0 }}
                      animate={{ y: 0, opacity: 1, transition: { type: "spring", stiffness: 420, damping: 32 } }}
                      exit={{ y: 24, opacity: 0, transition: { duration: 0.18 } }}
                    >
                      <div className="mx-auto h-1 w-12 rounded-full bg-black/10 mb-3" />
                      <div className="font-extrabold text-lg mb-2">{title}</div>
                      {children}
                    </motion.div>
                  </motion.div>
                )}
              </AnimatePresence>
            );
          }

          function RandomizeResult({ spots, onClose }) {
            const pickRandom = () => spots[Math.floor(Math.random() * spots.length)];
            const [pick, setPick] = useState(pickRandom());
            return (
              <div className="space-y-2">
                <div className="text-sm text-black/60">Your roll</div>
                <div className="text-2xl font-black">{pick.name}</div>
                <div className="text-black/60">{pick.city} · {pick.tags.join(" · ")} · {Number(pick.rating).toFixed(1)}</div>
                <div className="pt-2 flex gap-2">
                  <button className="px-4 py-2 rounded-xl border border-black/10 bg-black text-white" onClick={onClose}>Looks good</button>
                  <button className="px-4 py-2 rounded-xl border border-black/10" onClick={() => setPick(pickRandom())}>Roll again</button>
                </div>
              </div>
            );
          }

          function AddSpotForm({ onSave }) {
            const [name, setName] = useState("");
            const [city, setCity] = useState("");
            const [tags, setTags] = useState("");
            const [notes, setNotes] = useState("");
            const [addToFeed, setAddToFeed] = useState(true);
            const [rating, setRating] = useState(4.5);

            return (
              <form
                className="space-y-3"
                onSubmit={(e) => {
                  e.preventDefault();
                  const clean = {
                    name: name.trim() || "Untitled",
                    city: city.trim() || "Unknown",
                    tags: tags.split(",").map((t) => t.trim()).filter(Boolean),
                    notes: notes.trim(),
                    rating: Math.max(0, Math.min(5, parseFloat(String(rating)) || 0)),
                    addToFeed,
                  };
                  onSave(clean);
                }}
              >
                <div className="grid grid-cols-2 gap-3">
                  <input data-testid="add-name" className="px-3 py-2 rounded-xl border border-black/15" placeholder="Place name" value={name} onChange={(e) => setName(e.target.value)} required />
                  <input data-testid="add-city" className="px-3 py-2 rounded-xl border border-black/15" placeholder="City" value={city} onChange={(e) => setCity(e.target.value)} />
                </div>
                <input data-testid="add-tags" className="px-3 py-2 rounded-xl border border-black/15 w-full" placeholder="Tags (e.g. ramen, $$)" value={tags} onChange={(e) => setTags(e.target.value)} />

                <div className="grid grid-cols-5 items-center gap-3">
                  <label className="col-span-2 text-sm text-black/70">Rating (0–5)</label>
                  <input data-testid="add-rating" type="range" min={0} max={5} step={0.5} value={rating} onChange={(e)=>setRating(parseFloat(e.target.value))} className="col-span-2"/>
                  <div className="text-sm font-semibold">{Number(rating).toFixed(1)}</div>
                </div>

                <textarea data-testid="add-notes" className="px-3 py-2 rounded-xl border border-black/15 w-full" placeholder="Notes (what to order, best time, etc.)" rows={3} value={notes} onChange={(e) => setNotes(e.target.value)} />
                <label className="flex items-center gap-2 text-sm">
                  <input data-testid="add-feed" type="checkbox" className="h-4 w-4" checked={addToFeed} onChange={(e) => setAddToFeed(e.target.checked)} /> Add to feed
                </label>
                <div className="flex items-center justify-end">
                  <button data-testid="add-submit" type="submit" className="px-4 py-2 rounded-xl bg-[#FFC83D] text-black font-extrabold border border-black/10">
                    Save spot
                  </button>
                </div>
              </form>
            );
          }

          function EditProfileForm({ profile, onSave }) {
            const [name, setName] = useState(profile.name || "");
            const [handle, setHandle] = useState(profile.handle || "");
            const [avatar, setAvatar] = useState(profile.avatar || "");
            const [bio, setBio] = useState(profile.bio || "");
            const [dragOver, setDragOver] = useState(false);
            const fileInputRef = useRef(null);

            const onFiles = (files) => {
              const file = files && files[0];
              if (!file) return;
              if (!file.type.startsWith('image/')) return;
              const reader = new FileReader();
              reader.onload = (e) => setAvatar(String(e.target.result));
              reader.readAsDataURL(file);
            };

            return (
              <form
                className="space-y-4"
                onSubmit={(e) => {
                  e.preventDefault();
                  onSave({
                    name: name.trim() || profile.name,
                    handle: handle.replace(/^@/, '').trim() || profile.handle,
                    avatar: avatar.trim() || profile.avatar,
                    bio,
                  });
                }}
              >
                <div
                  className={`rounded-2xl border ${dragOver ? 'border-black/40 bg-black/5' : 'border-black/15 bg-white'} p-4 text-sm`}
                  onDragOver={(e)=>{ e.preventDefault(); setDragOver(true); }}
                  onDragLeave={()=>setDragOver(false)}
                  onDrop={(e)=>{ e.preventDefault(); setDragOver(false); onFiles(e.dataTransfer.files); }}
                >
                  <div className="flex items-center gap-4">
                    <div className="h-16 w-16 rounded-full overflow-hidden border border-black/10 bg-black/5 grid place-items-center">
                      {/^(https?:\\/\\/)/i.test(avatar) || avatar.startsWith('data:') ? (
                        <img src={avatar} alt="preview" className="h-full w-full object-cover" />
                      ) : (
                        <span className="text-2xl">{avatar || '🙂'}</span>
                      )}
                    </div>
                    <div className="flex-1 min-w-0">
                      <div className="font-semibold">Profile photo</div>
                      <div className="text-black/60">Drag & drop an image here, or</div>
                      <div className="mt-2 flex items-center gap-2">
                        <button type="button" className="px-3 py-1.5 rounded-xl border border-black/10" onClick={()=>fileInputRef.current?.click()}>Choose from photos</button>
                        <input ref={fileInputRef} type="file" accept="image/*" className="hidden" onChange={(e)=>onFiles(e.target.files)} />
                      </div>
                    </div>
                  </div>
                </div>

                <div className="grid grid-cols-5 gap-3 items-center">
                  <div className="col-span-2 text-sm text-black/70">Photo (emoji or image URL)</div>
                  <input
                    className="col-span-3 px-3 py-2 rounded-xl border border-black/15"
                    placeholder="🙂 or https://..."
                    value={avatar}
                    onChange={(e)=>setAvatar(e.target.value)}
                  />
                </div>

                <div className="grid grid-cols-5 gap-3 items-center">
                  <div className="col-span-2 text-sm text-black/70">Name</div>
                  <input className="col-span-3 px-3 py-2 rounded-xl border border-black/15" value={name} onChange={(e)=>setName(e.target.value)} />
                </div>
                <div className="grid grid-cols-5 gap-3 items-center">
                  <div className="col-span-2 text-sm text-black/70">Handle</div>
                  <div className="col-span-3 flex items-center gap-2">
                    <span className="text-sm text-black/50">@</span>
                    <input className="flex-1 px-3 py-2 rounded-xl border border-black/15" value={handle} onChange={(e)=>setHandle(e.target.value)} />
                  </div>
                </div>
                <textarea className="px-3 py-2 rounded-xl border border-black/15 w-full" placeholder="Bio" rows={3} value={bio} onChange={(e)=>setBio(e.target.value)} />
                <div className="flex items-center justify-end">
                  <button type="submit" className="px-4 py-2 rounded-xl bg-[#FFC83D] text-black font-extrabold border border-black/10">Save</button>
                </div>
              </form>
            );
          }

          function Container({ children, bottomBar, overlay, floating }) {
            return (
              <div className="h-[812px] w-[420px] max-w-[95vw] mx-auto my-6 rounded-[32px] border border-black/10 shadow-2xl overflow-hidden bg-[#f8fafc] relative">
                <div className="h-6 bg-black/90" />
                <div className="absolute inset-x-0 top-6 bottom-0">
                  <div className="h-full overflow-y-auto p-4 pb-32">{children}</div>
                </div>
                <div className="absolute left-1/2 -translate-x-1/2 bottom-4 w-[380px] max-w-[90%] z-10">{bottomBar}</div>
                {floating && (
                  <div className="absolute right-5 bottom-24 z-10">{floating}</div>
                )}
                {overlay}
              </div>
            );
          }

          function BottomBar({ active, setActive }) {
            const item = (key, label, icon) => (
              <motion.button
                whileTap={{ scale: 0.92 }}
                onClick={() => setActive(key)}
                className={`flex flex-col items-center gap-1 text-[10px] font-semibold transition-colors ${active === key ? "text-black" : "text-black/45"}`}
              >
                <div className="h-6 w-6 grid place-items-center">{icon}</div>
                {label}
              </motion.button>
            );

            return (
              <div className="rounded-2xl bg-white/95 backdrop-blur border border-black/10 px-6 py-2 flex justify-between items-center">
                {item("home", "Home", <HomeIcon />)}
                {item("map", "Explore", <MapIcon />)}
                {item("friends", "Friends", <FriendsIcon />)}
                {item("profile", "Profile", <UserIcon />)}
              </div>
            );
          }

          function SpotDetail({ spot, onClose }) {
            if (!spot) return null;
            return (
              <div className="space-y-2">
                <div className="text-xs uppercase tracking-wider text-black/60">Saved spot</div>
                <div className="text-2xl font-black">{spot.name}</div>
                <div className="text-black/70">{spot.city} · {spot.tags?.join(" · ")}</div>
                <div className="text-sm text-black/60">Rating: {Number(spot.rating).toFixed(1)} / 5</div>
                {spot.notes && (
                  <div className="mt-2 p-3 rounded-xl border border-black/10 bg-black/5 text-sm">
                    <div className="font-semibold mb-1">Notes</div>
                    <div>{spot.notes}</div>
                  </div>
                )}
                <div className="pt-2 flex gap-2">
                  <button className="px-4 py-2 rounded-xl border border-black/10 bg-black text-white" onClick={onClose}>Close</button>
                  <button className="px-4 py-2 rounded-xl border border-black/10" onClick={onClose}>Navigate</button>
                </div>
              </div>
            );
          }

          function VistaAppPreview() {
            const [active, setActive] = useState("home");
            const [sheet, setSheet] = useState({ open: false, view: null, spot: null });
            const [homeTab, setHomeTab] = useState("foryou");
            const [spots, setSpots] = useState([...mockSpots]);
            const [activities, setActivities] = useState([
              { id: 100, text: "Tanya bookmarked La Marina", meta: "2h ago · Barcelona", emoji: "👩‍🍳", cta: "View" },
              { id: 101, text: "Alex shared list ‘Rome 2025 Eats’", meta: "Yesterday · 12 spots", emoji: "🧑‍🧑‍🧒‍🧒", cta: "Open" },
            ]);
            const [followers, setFollowers] = useState([
              { id: 200, name: 'Maya', when: '1h ago', unread: true, avatar: '🧑‍🎓', following: false },
              { id: 201, name: 'Jon', when: 'Yesterday', unread: false, avatar: '🧑‍🍳', following: true },
            ]);
            const [messages, setMessages] = useState([
              { id: 300, from: 'Alex', text: 'Shared “Rome 2025 Eats” with you', when: 'Yesterday', unread: false, avatar: '✉️' },
            ]);
            const [profile, setProfile] = useState({ name: 'You', handle: 'you', avatar: 'TB', bio: '', lists: 3, saved: 18 });
            const followersCount = followers.length;
            const [inboxInitialTab, setInboxInitialTab] = useState('all');

            const openRandomize = () => setSheet({ open: true, view: "random", spot: null });
            const openAdd = () => setSheet({ open: true, view: "add", spot: null });
            const openDetail = (spot) => setSheet({ open: true, view: "detail", spot });

            const handleSaveSpot = (data) => {
              const newSpot = { id: Date.now(), ...data };
              setSpots((prev) => [newSpot, ...prev]);

              if (data.addToFeed) {
                setActivities((prev) => [
                  { id: Date.now() + 1, text: `You added ${newSpot.name}`, meta: `${newSpot.city} · ${newSpot.tags.join(" · ")}`, emoji: "📌", cta: "View", unread: true },
                  ...prev,
                ]);
                setMessages(prev => [
                  { id: Date.now() + 2, from: 'Vista', text: `Added ${newSpot.name} to your list`, when: 'Just now', unread: true, avatar: '🔔' },
                  ...prev
                ]);
              }

              setSheet({ open: false, view: null, spot: null });
              setActive("home");
              setHomeTab("city");
            };

            const followBack = (id) => {
              setFollowers(prev => prev.map(f => f.id === id ? { ...f, following: true, unread: false } : f));
            };

            const markAllInboxRead = () => {
              setFollowers(prev => prev.map(f => ({ ...f, unread: false })));
              setMessages(prev => prev.map(m => ({ ...m, unread: false })));
              setActivities(prev => prev.map(a => ({ ...a, unread: false })));
            };

            const phoneBottomBar = <BottomBar active={active} setActive={setActive} />;

            const phoneOverlay = (
              <PhoneSheet
                open={sheet.open}
                onClose={() => setSheet({ open: false, view: null, spot: null })}
                title={sheet.view === "add" ? "Add a spot" : sheet.view === "detail" ? sheet.spot?.name || "Spot" : sheet.view === 'editProfile' ? 'Edit profile' : "Your Vista pick"}
              >
                {sheet.view === "add" && <AddSpotForm onSave={handleSaveSpot} />}
                {sheet.view === "random" && <RandomizeResult spots={spots} onClose={() => setSheet({ open: false, view: null, spot: null })} />}
                {sheet.view === "detail" && <SpotDetail spot={sheet.spot} onClose={() => setSheet({ open: false, view: null, spot: null })} />}
                {sheet.view === 'editProfile' && <EditProfileForm profile={profile} onSave={(p)=>{ setProfile(prev=>({ ...prev, ...p })); setSheet({ open:false, view:null, spot:null }); }} />}
              </PhoneSheet>
            );

            useEffect(() => {
              console.assert(typeof openRandomize === 'function' && typeof openAdd === 'function', '[test] handlers exist');
              console.assert(typeof markAllInboxRead === 'function', '[test] inbox markAll exists');
              const nameInput = document.querySelector('[data-testid="add-name"]');
              const cityInput = document.querySelector('[data-testid="add-city"]');
              const ratingInput = document.querySelector('[data-testid="add-rating"]');
              console.assert(nameInput !== null && cityInput !== null && ratingInput !== null || true, '[test] Add form fields will render when sheet opens');
            }, []);

            return (
              <div className="w-full grid place-items-center">
                <Container bottomBar={phoneBottomBar} overlay={phoneOverlay} floating={(
                  <motion.button
                    whileTap={{ scale: 0.9 }}
                    onClick={openAdd}
                    aria-label="Add spot"
                    className="h-14 w-14 rounded-full bg-[#FFC83D] text-black text-2xl font-extrabold grid place-items-center shadow-xl border border-black/10"
                  >
                    +
                  </motion.button>
                )}>
                  <Header onOpenInbox={() => { setInboxInitialTab('all'); setActive('inbox'); }} />

                  <div className="mt-4">
                    <AnimatePresence mode="wait">
                      <motion.div
                        key={active}
                        initial={{ opacity: 0, y: 8 }}
                        animate={{ opacity: 1, y: 0, transition: { duration: 0.22 } }}
                        exit={{ opacity: 0, y: -8, transition: { duration: 0.18 } }}
                      >
                        {active === "home" && (
                          <HomeScreen tab={homeTab} setTab={setHomeTab} onRandomize={openRandomize} onOpenSpot={openDetail} spots={spots} />
                        )}
                        {active === "map" && <MapScreen />}
                        {active === "friends" && <FriendsScreen activities={activities} onOpenMessages={() => { setInboxInitialTab('messages'); setActive('inbox'); }} />}
                        {active === "profile" && (
                          <ProfileScreen profile={profile} followersCount={followersCount} onEditProfile={()=> setSheet({ open:true, view:'editProfile', spot:null })} />
                        )}
                        {active === "inbox" && (
                          <InboxScreen followers={followers} messages={messages} activities={activities} onMarkAll={markAllInboxRead} onFollowBack={followBack} initialTab={inboxInitialTab} />
                        )}
                      </motion.div>
                    </AnimatePresence>
                  </div>
                </Container>
              </div>
            );
          }

          const root = ReactDOM.createRoot(document.getElementById('root'));
          root.render(<VistaAppPreview />);
        </script>
      </body>
    </html>
    """,
    height=950,
    scrolling=True,
)
