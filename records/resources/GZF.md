---
records:
    - id: GZFYQ9EKPG
      kind: monograph
      title: Group Theory and Quantum Mechanics
      creators:
        - name: B. L. van der Waerden
          role: author
      date: "1974"
      msc:
        - code: 22-02
          from: zbmath_search
        - code: "22E45"
          from: zbmath_search
        - code: "22E43"
          from: zbmath_search
        - code: "22E70"
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "1974"
          ids:
            doi: 10.1007/978-3-642-65860-0
            zbl: "0301.22001"
            zbl_id: "3470697"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1974"
              ids:
                isbn:
                    - "9783642658624"
                    - "9783642658600"
              access:
                class: record
      relations:
        - kind: part_of
          to: GQFCNY816R
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 dev scope/1
      catalogue:
        - source: crossref_language
          snapshot: blake3:99510ada1a0f54f83dbf4ed97ef48852461d1f98d338d1a350cabf222fb85948
          native_id: 10.1007/978-3-642-65860-0
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-642-65860-0
          level: work
        - source: zbmath_search
          snapshot: blake3:25dd7c4358839cf7c8c9f5d07f0562e94f38728153e7db2255a7191282b967c2
          native_id: "3470697"
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
          at: "2026-11-02"
          by: m2 v0.6.17 scope/1
          note: from in to in
---
