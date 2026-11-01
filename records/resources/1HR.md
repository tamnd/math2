---
records:
    - id: 1HRPTPSVEH
      kind: problem-set
      title: Kvant 2025, no. 8
      creators:
        - name: Kvant editorial board
          role: editor
      date: "2025"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "2025"
          structure: 1HRPTPSVEH/e1.json
      relations:
        - kind: part_of
          to: W84MAFPC23
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: kvant
          snapshot: blake3:9ef7ec326c8e38c2cc1957ddca07480f15b4e9ef49d8059191fc4a1c78c7cd39
          native_id: 2025-8
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
    - id: 1HRYZBB5NE
      kind: monograph
      title: The Group Theory Puzzle Book
      creators:
        - name: David Nacin
          role: author
          ids:
            orcid: 0000-0002-3994-9729
      date: "2024"
      msc:
        - code: 20-01
          from: zbmath_search
        - code: 00A08
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2024"
          ids:
            doi: 10.1007/978-3-031-70091-0
            zbl: "1551.20001"
            zbl_id: "7938930"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Nature Switzerland
              date: "2024"
              ids:
                isbn:
                    - "9783031700903"
                    - "9783031700910"
              access:
                class: record
      relations:
        - kind: part_of
          to: 3YXAC8SZBF
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.14 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-031-70091-0
          level: work
        - source: zbmath_search
          snapshot: blake3:c337ce98d6a5f313c8656eac90c3348668181c9ed20fe8fe7554afd8dc3904ca
          native_id: "7938930"
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
---
