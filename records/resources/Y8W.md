---
records:
    - id: Y8W4ZBPVBP
      kind: problem-set
      title: Kvant 1977, no. 11
      creators:
        - name: Kvant editorial board
          role: editor
      date: "1977"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "1977"
          structure: Y8W4ZBPVBP/e1.json
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
          native_id: 1977-11
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
    - id: Y8WFNMJ1K7
      kind: monograph
      title: Information Geometry
      creators:
        - name: Khadiga A. Arwini
          role: author
        - name: Christopher T. J. Dodson
          role: author
      date: "2008"
      msc:
        - code: 62M99
          from: zbmath_search
        - code: 62B10
          from: zbmath_search
        - code: 62Pxx
          from: zbmath_search
        - code: 53Z99
          from: zbmath_search
        - code: 62-01
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2008"
          ids:
            doi: 10.1007/978-3-540-69393-2
            zbl: "1269.62070"
            zbl_id: "5306298"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "2008"
              ids:
                isbn:
                    - "9783540693918"
                    - "9783540693932"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-540-69393-2
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "5306298"
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
