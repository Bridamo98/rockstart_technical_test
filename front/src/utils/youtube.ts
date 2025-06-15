export function extractYoutubeId(url: string): string | null {
  const reg = /(?:youtube\.com\/watch\?v=|youtu\.be\/)([A-Za-z0-9_-]{11})/;
  const match = url.match(reg);
  return match ? match[1] : null;
}

export function isYoutubeUrl(url: string): boolean {
  return !!extractYoutubeId(url);
}
