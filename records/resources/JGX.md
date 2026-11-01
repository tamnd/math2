---
records:
    - id: JGX7MYQ78W
      kind: problem-set
      title: Kvant 1996, no. 1
      creators:
        - name: Kvant editorial board
          role: editor
      date: "1996"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "1996"
          structure: JGX7MYQ78W/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 1996-1
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: from in to in
    - id: JGXPCGFRNH
      kind: monograph
      title: Minimal Surfaces, Stratified Multivarifolds, and the Plateau Problem
      creators:
        - name: Dao Thi
          role: author
        - name: A. Fomenko
          role: author
      date: "1991-02-21"
      msc:
        - code: 53-XX
          from: classify/1@2b838f8bc9d8
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1991-02-21"
          ids:
            doi: 10.1090/mmono/084
          manifestations:
            - key: m1
              kind: print
              publisher: American Mathematical Society
              date: "1991-02-21"
              ids:
                isbn:
                    - "9780821845363"
                    - "9780821898277"
                    - "9781470444976"
              access:
                class: record
      relations:
        - kind: part_of
          to: BTDY0N3WC9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: ams-series
          snapshot: blake3:caf23f13a44130cfaf0ea65e08f1b670683c2f34af9ccb44343f3bca428b1013
          native_id: 10.1090/mmono/084
          level: work
        - source: crossref_language
          snapshot: blake3:78a08c6dff20a47d6ad06a8fc0424f997c851421644ee012bc0f425814d0a6d5
          native_id: 10.1090/mmono/084
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
