---
records:
    - id: YK8C960QCD
      kind: problem-set
      title: Kvant 1975, no. 7
      creators:
        - name: Kvant editorial board
          role: editor
      date: "1975"
      msc:
        - code: 00A07
          from: kvant
        - code: 97U40
          from: kvant
      expressions:
        - key: e1
          kind: edition
          language: ru
          date: "1975"
          structure: YK8C960QCD/e1.json
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
          native_id: 1975-7
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
    - id: YK8KPZZQ6Z
      kind: monograph
      title: 'Symmetry in Geometry and Analysis, Volume 3: Festschrift in Honor of Toshiyuki Kobayashi'
      creators:
        - name: Michael Pevzner
          role: editor
          ids:
            orcid: 0000-0001-9166-2373
        - name: Hideko Sekiguchi
          role: editor
      date: "2025"
      msc:
        - code: 22-06
          from: zbmath_search
        - code: "22E46"
          from: zbmath_search
        - code: "22E47"
          from: zbmath_search
        - code: 42-06
          from: zbmath_search
        - code: 43-06
          from: zbmath_search
        - code: 43A85
          from: zbmath_search
        - code: 00B25
          from: zbmath_search
        - code: 00B30
          from: zbmath_search
      expressions:
        - key: e1
          kind: edition
          language: en
          date: "2025"
          ids:
            doi: 10.1007/978-981-97-7666-5
            zbl: "1560.22004"
            zbl_id: "7951991"
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Nature Singapore
              date: "2025"
              ids:
                isbn:
                    - "9789819776658"
                    - "9789819776665"
              access:
                class: record
      relations:
        - kind: part_of
          to: VS2PFDMCR5
          source: cluster/1
      scope:
        value: in
        rule: S1
        by: m2 v0.6.16 scope/1
      catalogue:
        - source: crossref_language
          snapshot: blake3:78a08c6dff20a47d6ad06a8fc0424f997c851421644ee012bc0f425814d0a6d5
          native_id: 10.1007/978-981-97-7666-5
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-981-97-7666-5
          level: work
        - source: zbmath_search
          snapshot: blake3:928c873c1dac6852b2bf2c77184182759305f81342a4dc8ca5c0d4768bc6dd1e
          native_id: "7951991"
          level: work
      history:
        - op: add
          at: "2026-11-01"
          by: m2 v0.6.13 cluster/1
        - op: split
          at: "2026-11-01"
          by: m2 v0.6.13 cluster/1
          note: split from 9XM9WPH7G5
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.13 scope/1
          note: to in
        - op: scope
          at: "2026-11-01"
          by: m2 v0.6.14 scope/1
          note: from in to in
---
