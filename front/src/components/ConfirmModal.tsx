import Modal from "./Modal";

interface Props {
  open: boolean;
  title?: string;
  message?: string;
  confirmLabel?: string;
  cancelLabel?: string;
  onConfirm: () => void;
  onCancel: () => void;
}

export default function ConfirmModal({
  open,
  title = "Confirm",
  message = "Are you sure?",
  confirmLabel = "Yes",
  cancelLabel = "Cancel",
  onConfirm,
  onCancel,
}: Props) {
  return (
    <Modal open={open} onClose={onCancel}>
      <h3 className="text-lg font-semibold mb-3">{title}</h3>
      <p className="mb-6">{message}</p>
      <div className="flex justify-end gap-2">
        <button onClick={onCancel} className="btn btn-secondary">
          {cancelLabel}
        </button>
        <button onClick={onConfirm} className="btn btn-error">
          {confirmLabel}
        </button>
      </div>
    </Modal>
  );
}
