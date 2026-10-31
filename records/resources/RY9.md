---
records:
    - id: RY96RV6AA3
      kind: edited-volume
      title: Modern Algebra Volume 1
      creators:
        - name: O. Bezushchak
          role: editor
        - name: Yu. Drozd
          role: editor
        - name: P. Etingof
          role: editor
        - name: V. Futorny
          role: editor
        - name: R. Grigorchuk
          role: editor
        - name: E. Zelmanov
          role: editor
      date: "2025-11-19"
      expressions:
        - key: e1
          kind: edition
          date: "2025-11-19"
          ids:
            doi:
                - 10.1090/conm/829
                - 10.1090/conm/830
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "2025-11-19"
              ids:
                isbn:
                    - "9781470481049"
                    - "9781470476199"
            - key: m2
              kind: print
              publisher: American Mathematical Society
              date: "2025-12-02"
              ids:
                isbn:
                    - "9781470481056"
                    - "9781470476205"
      relations:
        - kind: part_of
          to: VAEN3CBGT1
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/829
          level: work
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/conm/830
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
