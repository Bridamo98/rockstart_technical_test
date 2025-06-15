import { extractYoutubeId } from "../utils/youtube";

interface Props {
  url: string;
}
export default function VideoPlayer({ url }: Props) {
  const id = extractYoutubeId(url);
  if (!id) return <p className="text-red-500">URL inválida</p>;
  return (
    <div className="aspect-video">
      <iframe
        title={`video_${id}`}
        className="w-full h-full"
        src={`https://www.youtube.com/embed/${id}`}
        allowFullScreen
      />
    </div>
  );
}
